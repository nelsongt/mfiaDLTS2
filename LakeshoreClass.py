# Copyright George Nelson 2021
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
        
        self.sample_sensor = ''
        self.control_sensor = ''
        self.heater_range = ''

    def reset(self,lake):
        self.generate_log("Initializing Lakeshore...","blue")
        self.stopped = False

        self.sample_sensor = lake.sample
        self.control_sensor = lake.control
        self.heater_range = lake.heatpower

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
        idnCheck330 = 'LSCI,MODEL330';
        cut = len(idnCheck)
        if idn[0:cut] == idnCheck330:
            return True
        else:
            return False

    def isLakeshoreConfigured(self,lake):
        config_string = self.control_sensor + ',1,0,2'    # Control sensor A or B, in Kelvin (1), default heater off (0), heater units power (2)
        response = self.lakeshoreQuery('CSET?')
        if response != config_string:
            self.obj1.write('CSET 1,' + config_string)       # Control loop 1, then config string above
        elif response == '-1':
            return False

        range_string = self.heater_range
        response = self.lakeshoreQuery('RANGE?')
        if response != lake.heatpower:
            self.obj1.write('RANGE ' + lake.heatpower) # Set heater to high (3), medium (2), low (1)
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
        if self.sample_sensor == 'A':
            try:
                temp = self.obj1.temperature_A
                return temp
            except:
                self.lakeshore_disconnect.emit()
        elif self.sample_sensor == 'B':
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
        while (abs(getCurrentTemp - setPoint) > tempStable or getCurrentWait >= 1) and self.stopped == False:  # Continuously loop the time and temp stability until both are met
            while abs(getCurrentTemp - setPoint) > tempStable and not self.stopped:
                time.sleep(2)  # Wait for temperature to reach set point
                getCurrentTemp = self.sampleSpaceTemperature()
                #getCurrentTemp = setPoint
                self.generate_log("Current Temp: {:3.2f}. Set point: {:3.2f}. Delta: {:2.2f}.".format(getCurrentTemp,setPoint,getCurrentTemp-setPoint),"blue")
            unstable = False;
            while getCurrentWait >= 1 and not unstable and not self.stopped:
                self.generate_log("Wait for time stability: {:d} s left.".format(getCurrentWait),"blue")
                time.sleep(1)                          # Wait 1 second
                getCurrentWait = getCurrentWait - 1          # Subtract one from our counter
                getCurrentTemp = self.sampleSpaceTemperature()
                if abs(getCurrentTemp - setPoint) > tempStable:  # check again for temp stability, if not stable then flag for restart
                    unstable = True

            if unstable:  # check again for temp stability, if not stable then restart process
                getCurrentWait = timeStable
                self.generate_log("Temperature not time stable (refine PID?), restarting stability process...","orange") #TODO color [0.9100 0.4100 0.1700]? orange?
        if self.stopped == False:
            self.generate_log("Temperature has stabilized!","green")