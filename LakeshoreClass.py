# Copyright George Nelson 2020
# Lakeshore class, generates instances of Lakeshore virtual interface

import time
from PyQt5.QtCore import pyqtSignal
from pymeasure.instruments.lakeshore import LakeShore331

from LogClass import LogObject


class Lakeshore(LogObject):
    lakeshore_disconnect = pyqtSignal()

    def __init__(self):
        super(Lakeshore, self).__init__()
        self.obj1 = []

        # Stopped state for when user clicks stop
        self.stopped = []

    def reset(self):
        self.generate_log("Initializing Lakeshore...","blue")
        self.stopped = False

        # Check for lakeshore 331
        try:
            self.obj1 = LakeShore331("GPIB0::12")
        except:
            self.generate_log("Could not initialize GPIB interface. Make sure drivers are installed.","red")
            return False
        if self.isLakeshoreConnected() == False:
            self.generate_log("Lakeshore Not Found. Connect and re-initialize.","orange")
            self.obj1 = []
            return False

        # Setup Lakeshore
        if self.isLakeshoreConfigured() == False:
            self.generate_log("Lakeshore Could Not Be Configured. Troubleshoot and re-initialize.","orange")
            self.obj1 = []
            return False

        self.generate_log("Lakeshore configure OK.","Green")
        return True

    def isLakeshoreConnected(self):
        # Initialize communication to temperature controller. Requires PyMeasure

        # Attempt to communicate, if fail catch error
        try:
            idn = self.obj1.id
        except:
            return False

        # Make sure device is a lakeshore
        idnCheck = 'LSCI,MODEL330,0,032301';
        if idn == idnCheck:
            return True
        else:
            return False

    def isLakeshoreConfigured(self):
        response = self.lakeshoreQuery('CSET?')
        if response != 'B,1,0,2':
            self.obj1.write('CSET 1,B,1,0,2') # Control loop 1, sensor B, in Kelvin (1), default heater off (0), heater units power (2)
        elif response == '-1':
            return False

        response = self.lakeshoreQuery('RANGE?')
        if response != '3':
            self.obj1.write('RANGE 3') # Set heater to high (3), medium (2), low (1)
        elif response == '-1':
            return False

        return True

    def lakeshoreQuery(self,command):
        try:
            response = self.obj1.ask(command).rstrip()
            return response
        except:
            self.generate_log("Lakeshore connection problem.","red")
            return '-1'

    def sampleSetPoint(self,point):
        try:
            self.obj1.write('SETP {:3.2f}'.format(point))
        except:
            self.generate_log("Lakeshore connection problem.","red")
            self.lakeshore_disconnect.emit()

    def sampleSpaceTemperature(self):
        # Get the temperature
        try:
            temp = self.obj1.temperature_B
            return temp
        except:
            self.lakeshore_disconnect.emit()


    def SET_TEMP(self,setPoint,tempStable,timeStable):
        self.sampleSetPoint(setPoint)  # Set point to lakeshore
        getCurrentTemp = self.sampleSpaceTemperature()
        #getCurrentTemp = 290
        getCurrentWait = timeStable
        unstable = False
        while (abs(getCurrentTemp - setPoint) > tempStable or getCurrentWait >= 0) and self.stopped == False:  # Continuously loop the time and temp stability until both are met
            while abs(getCurrentTemp - setPoint) > tempStable and self.stopped == False:
                time.sleep(2)  # Wait for temperature to reach set point
                getCurrentTemp = self.sampleSpaceTemperature()
                #getCurrentTemp = setPoint
                self.generate_log("Current Temp: {:3.2f}. Set point: {:3.2f}. Delta: {:2.2f}.".format(getCurrentTemp,setPoint,getCurrentTemp-setPoint),"blue")
            unstable = False;
            while getCurrentWait >= 0 and unstable == False and self.stopped == False:
                self.generate_log("Wait for time stability: {:d} s left.".format(getCurrentWait),"blue")
                time.sleep(1)                          # Wait 1 second
                getCurrentWait = getCurrentWait - 1          # Subtract one from our counter
                getCurrentTemp = self.sampleSpaceTemperature()
                if abs(getCurrentTemp - setPoint) > tempStable:  # check again for temp stability, if not stable then flag for restart
                    unstable = True

            if unstable == True:  # check again for temp stability, if not stable then restart process
                getCurrentWait = timeStable
                self.generate_log("Temperature not time stable (refine PID?), restarting stability process...","orange") #TODO color [0.9100 0.4100 0.1700]? orange?
        if self.stopped == False:
            self.generate_log("Temperature has stabilized!","green")