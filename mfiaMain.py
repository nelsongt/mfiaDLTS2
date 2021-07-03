# Copyright George Nelson 2021
# Main file

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import pyqtgraph as pg
import numpy as np

from MainWindow import Ui_MainWindow
from GraphClass import MultiLine
from WorkerClass import AcquireData
from ParamsClass import SampleParams,DLTSParams,TempParams,LakeshoreParams,MFIAParams


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.first_plot = True
        self.curves = []

        ## CREATE PARAM STRUCTS
        self.sample = SampleParams()
        self.dlts = DLTSParams()
        self.temp = TempParams()
        self.lake = LakeshoreParams()
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
        self.data.lakeshore.lakeshore_disconnect.connect(self.stopping_scan)
        self.data.lakeshore.lakeshore_disconnect.connect(self.state_stopwait)
        self.data.graph_update.connect(self.graph_data)
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
        
        # Set Lakeshore parameters
        if self.radioSampleA.isChecked() == True:
            self.lake.sample = 'A'
        elif self.radioSampleB.isChecked() == True:
            self.lake.sample = 'B'
        if self.radioControlA.isChecked() == True:
            self.lake.control = 'A'
        elif self.radioControlB.isChecked() == True:
            self.lake.control = 'B'
        if self.radioHeaterLow.isChecked() == True:
            self.lake.heatpower = '1'
        elif self.radioHeaterMed.isChecked() == True:
            self.lake.heatpower = '2'
        elif self.radioHeaterHi.isChecked() == True:
            self.lake.heatpower = '3'            

        # Set MFIA Parameters
        self.mfia.sample_rate = self.mfiaSample.value()
        self.mfia.ac_freq = self.mfiaFreq.value()
        self.mfia.ac_ampl = self.mfiaAmp.value()
        self.mfia.time_constant = self.mfiaTC.value()


        ## INITIALIZE WORKER
        self.data.reset(self.sample,self.dlts,self.temp,self.lake,self.mfia)

    def graph_data(self):
        #nPlots = 100
        nPlots = self.data.cap_data.shape[1]
        #nSamples = 16000
        nSamples = self.data.cap_data.shape[0]
        #y = np.random.normal(size=(120,20000), scale=0.2) + np.arange(120)[:,np.newaxis]
        #x = np.empty((120,20000))
        #x[:] = np.arange(20000)[np.newaxis,:]
        now = pg.ptime.time()
        if self.first_plot:
            #data = np.random.normal(size=(nPlots,nSamples))
            self.graphWidget.disableAutoRange()
            self.graphWidget.setYRange(np.nanmin(self.data.cap_data), np.nanmax(self.data.cap_data))
            self.graphWidget.setXRange(0, nSamples)

            for idx in range(nPlots):
                curve = pg.PlotCurveItem(pen=(170-idx,nPlots*4))  #7->17 out of 40
                self.graphWidget.addItem(curve)
                self.curves.append(curve)
                #lines = MultiLine(x,y)
                self.curves[idx].setData(self.data.cap_data[:,idx])
            curve = pg.PlotCurveItem(pen='r')
            self.graphWidget.addItem(curve)
            self.curves.append(curve)
            self.curves[nPlots].setData(self.data.file.transient)
            #lines = MultiLine(x,y)
            #self.graphWidget.addItem(lines)

            self.first_plot = False
        else:
            #data = np.random.normal(size=(nPlots,nSamples))
            print('hi')
            self.graphWidget.setYRange(np.nanmin(self.data.cap_data), np.nanmax(self.data.cap_data))
            self.graphWidget.setXRange(0, nSamples)
            for idx in range(nPlots):
                self.curves[idx].setData(self.data.cap_data[:,idx])
            self.curves[nPlots].setData(self.data.file.transient)
        print("Plot time: %0.2f sec" % (pg.ptime.time()-now))
        app.processEvents()

    def commence_scan(self):
        self.thread.start()

    def stopping_scan(self):
        self.generate_log("Stop signal sent. Please wait...","orange")
        self.data.lakeshore.stopped = True

    def scan_complete(self):
        self.first_plot = True
        self.curves = []
        self.generate_log("All done.","green")



app = QtWidgets.QApplication(sys.argv)



window = MainWindow()
window.show()
app.exec()
