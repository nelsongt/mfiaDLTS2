# Copyright George Nelson 2020
# Worker thread

import time
import math
import numpy
from PyQt5.QtCore import pyqtSignal,pyqtSlot

from LogClass import LogObject
from LakeshoreClass import Lakeshore
from MFIAClass import MFIA
from FileClass import FileSave


class AcquireData(LogObject):
    init_fail = pyqtSignal()  # Cannot put signals in constructor(?)
    graph_update = pyqtSignal()

    def __init__(self):
        super(AcquireData, self).__init__()

        ## LOCAL VARS
        #self.device_id = []
        self.cap_data = []
        self.avg_trnst = []

        ## CREATE PARAM STRUCTS
        self.sample = []
        self.dlts = []
        self.temp = []
        self.mfia = []

        ## CREATE HARDWARE INSTANCES
        self.lakeshore = Lakeshore()
        self.device = MFIA()

        ## CREATE FILE SAVE SUBWORKER
        self.file = FileSave(1)

    def reset(self,sampleParam,dltsParam,tempParam,mfiaParam):
        ## SYNC PARAM STRUCTS FROM UI
        self.sample = sampleParam
        self.dlts = dltsParam
        self.temp = tempParam
        self.mfia = mfiaParam
        
        self.graph_update.emit()

        ## INITIALIZE HARDWARE
        if self.lakeshore.reset() == False: # Now initialize Lakeshore
            self.init_fail.emit()
            return
        self.device.reset(self.dlts,self.mfia) # Now initialize MFIA

    @pyqtSlot()
    def stop_signal(self):
        self.lakeshore.stopped = True;

    @pyqtSlot()
    def do_scan(self):
        current_temp = self.temp.temp_init;
        current_num = 0;
        steps = math.ceil(abs(self.temp.temp_init - self.temp.temp_final)/self.temp.temp_step);
        while current_num <= steps and not self.lakeshore.stopped:
            self.generate_log("Waiting for set point {}... ".format(current_temp),"blue")
            time.sleep(1)
            self.lakeshore.SET_TEMP(current_temp,self.temp.temp_stability,self.temp.time_stability) #Wait for lakeshore to reach set temp

            if not self.lakeshore.stopped:
                # Capture transient data from MFIA
                self.generate_log("Capturing transient...","blue")
                temp_before  = self.lakeshore.sampleSpaceTemperature();
                #[timestamp, sampleCap] = MFIA_CAPACITANCE_POLL(device,mfia); #TODO implement constant polling?
                self.cap_data = self.device.MFIA_CAPACITANCE_DAQ(self.dlts,self.mfia)*1e12
                temp_after = self.lakeshore.sampleSpaceTemperature();
                avg_temp = (temp_before + temp_after) / 2;
                self.generate_log("Finished transient for this temperature.","green")

                # Find the amount of data loss, if more than a few percent lower duty cycle or lower sampling rate
                dataloss = numpy.sum(numpy.isnan(self.cap_data))/numpy.size(self.cap_data)
                if dataloss:
                    #cprintf('systemcommands', 'Warning: %1.1f%% data loss detected.\n',100*dataloss);
                    self.generate_log("Warning: {:1.1f}% data loss detected.".format(dataloss*100),"orange")

                #avg_trnst = MFIA_TRANSIENT_AVERAGER_POLL(sampleCap,mfia); #Not implemented in python yet
                self.file.transient = MFIA_TRANSIENT_AVERAGER_DAQ(sampleCap,mfia)
                self.graph_update.emit()
        
                self.generate_log("Saving transient...","blue")
                self.file.TRANSIENT_FILE(self.sample,self.dlts,self.mfia,current_num,current_temp,avg_temp)
        #
            if self.temp.temp_init > self.temp.temp_final:
                current_temp = current_temp - self.temp.temp_step    # Changes +/- for up vs down scan
            elif self.temp.temp_init < self.temp.temp_final:
                current_temp = current_temp + self.temp.temp_step
            current_num = current_num + 1

        if not self.lakeshore.stopped:
            self.generate_log("Finished data collection, returning to idle temp.","blue")
            self.lakeshore.SET_TEMP(self.temp.temp_idle,self.temp.temp_stability,self.temp.time_stability) # Wait for lakeshore to reach set temp
        elif self.lakeshore.stopped:
            self.generate_log("Stop successful.","orange")
        self.finished.emit()


