# Copyright George Nelson 2020
# Main file

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread

from MainWindow import Ui_MainWindow
from WorkerClass import AcquireData
from ParamsClass import SampleParams,DLTSParams,TempParams,MFIAParams


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        ## CREATE PARAM STRUCTS
        self.sample = SampleParams()
        self.dlts = DLTSParams()
        self.temp = TempParams()
        self.mfia = MFIAParams()

        ## CREATE PRIMARY WORKER THREAD
        self.data = AcquireData()
        self.thread = QThread()
        self.data.moveToThread(self.thread)
        self.data.finished.connect(self.thread.quit)
        self.thread.started.connect(self.data.do_scan)

        ## MAIN SIGNAL->SLOTS
        # Machine States
        self.buttonInit.clicked.connect(self.initialize_hardware)
        self.buttonStart.clicked.connect(self.commence_scan)
        self.buttonStop.clicked.connect(self.stopping_scan)
        self.data.init_fail.connect(self.scan_complete)
        self.data.init_fail.connect(self.state_stopped)
        self.data.finished.connect(self.scan_complete)
        self.data.finished.connect(self.state_stopped)

        # Worker LogObjects may print to log
        self.data.log_signal.connect(self.generate_log)
        self.data.lakeshore.log_signal.connect(self.generate_log)
        self.data.device.log_signal.connect(self.generate_log)
        self.data.file.log_signal.connect(self.generate_log)

    def initialize_hardware(self):
        ## POPULATE PARAMS STRUCTS FROM UI
        self.generate_log("All settings now locked in. You must re-initialize to make changes.")
        # Set sample info
        self.sample.user = self.sampleUser.text()
        self.sample.name = self.sampleName.text()
        self.sample.material = self.sampleMat.text()
        self.sample.area = self.sampleArea.value()
        self.sample.comment = self.sampleComment.text()

        # Set DLTS experiment parameters
        self.dlts.ss_bias = self.dltsBias.value()
        self.dlts.pulse_height = self.dltsPulse.value()
        self.dlts.trns_length = self.dltsTWidth.value()
        self.dlts.pulse_width = self.dltsPWidth.value()
        self.dlts.sample_time = self.dltsSample.value()

        # Set temperature parameters
        self.temp.temp_init = self.tempStart.value()
        self.temp.temp_step = self.tempStep.value()
        self.temp.temp_final = self.tempEnd.value()
        self.temp.temp_idle = self.tempIdle.value()
        self.temp.temp_stability = self.tempStable.value()
        self.temp.time_stability = self.timeStable.value()

        # Set MFIA Parameters
        self.mfia.sample_rate = self.mfiaSample.value()
        self.mfia.ac_freq = self.mfiaFreq.value()
        self.mfia.ac_ampl = self.mfiaAmp.value()
        self.mfia.time_constant = self.mfiaTC.value()


        ## INITIALIZE WORKER
        self.data.reset(self.sample,self.dlts,self.temp,self.mfia)


    def commence_scan(self):
        self.thread.start()

    def stopping_scan(self):
        self.generate_log("Stop signal sent. Please wait...","orange")
        self.data.lakeshore.stopped = True;

    def scan_complete(self):
        self.generate_log("All done.","green")



app = QtWidgets.QApplication(sys.argv)



window = MainWindow()
window.show()
app.exec()
