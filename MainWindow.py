# Copyright George Nelson 2021
# UI Class, UI-related code goes here

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from scientificspin import ScientificDoubleSpinBox
import pyqtgraph as pg
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        
        ## MAIN LAYOUT
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("""
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 1px;
                padding: 2px 5px 0px 5px;
                }
            """)

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")

        self.topLayout = QtWidgets.QHBoxLayout()
        self.topLayout.setObjectName("topLayout")
        self.mainLayout.addLayout(self.topLayout)
        
        
        ## BUTTONS
        # SETUP ROWS
        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.topLayout.addLayout(self.buttonLayout)
        
        self.buttonRow1 = QtWidgets.QHBoxLayout()
        self.buttonRow1.setObjectName("buttonRow1")
        self.buttonLayout.addLayout(self.buttonRow1)
        
        self.buttonRow2 = QtWidgets.QHBoxLayout()
        self.buttonRow2.setObjectName("buttonRow2")
        self.buttonLayout.addLayout(self.buttonRow2)

        self.buttonRow3 = QtWidgets.QHBoxLayout()
        self.buttonRow3.setObjectName("buttonRow3")
        self.buttonLayout.addLayout(self.buttonRow3)
        
        self.buttonRow4 = QtWidgets.QHBoxLayout()
        self.buttonRow4.setObjectName("buttonRow4")
        self.buttonLayout.addLayout(self.buttonRow4)

        self.buttonRow5 = QtWidgets.QHBoxLayout()
        self.buttonRow5.setObjectName("buttonRow5")
        self.buttonLayout.addLayout(self.buttonRow5)
        
        self.buttonRow6 = QtWidgets.QHBoxLayout()
        self.buttonRow6.setObjectName("buttonRow6")
        self.buttonLayout.addLayout(self.buttonRow6)
        
        # ROW 1 SAMPLE
        self.sampleBox = QtWidgets.QGroupBox('Sample Parameters')
        self.sampleBox.setObjectName("sampleBox")
        #self.sampleBox.setFlat(True)
        self.buttonRow1.addWidget(self.sampleBox)
        
        self.sampleLayout = QtWidgets.QGridLayout()
        self.sampleLayout.setObjectName("sampleLayout")
        self.sampleBox.setLayout(self.sampleLayout)
        
        self.sampleUserLabel = QtWidgets.QLabel('User:')
        self.sampleUserLabel.setObjectName("sampleUserLabel")
        self.sampleLayout.addWidget(self.sampleUserLabel,0,0)
        
        self.sampleUser = QtWidgets.QLineEdit()
        self.sampleUser.setObjectName("sampleUser")
        self.sampleLayout.addWidget(self.sampleUser,0,1)

        self.sampleNameLabel = QtWidgets.QLabel('Sample Name:')
        self.sampleNameLabel.setObjectName("sampleNameLabel")
        self.sampleLayout.addWidget(self.sampleNameLabel,1,0)

        self.sampleName = QtWidgets.QLineEdit()
        self.sampleName.setObjectName("sampleName")
        self.sampleLayout.addWidget(self.sampleName,1,1)

        self.sampleMatLabel = QtWidgets.QLabel('Sample Material:')
        self.sampleMatLabel.setObjectName("sampleMatLabel")
        self.sampleLayout.addWidget(self.sampleMatLabel,0,2)
        
        self.sampleMat = QtWidgets.QLineEdit()
        self.sampleMat.setObjectName("sampleMat")
        self.sampleLayout.addWidget(self.sampleMat,0,3)

        self.sampleAreaLabel = QtWidgets.QLabel('Sample Area (mm<sup>2</sup>):')
        self.sampleAreaLabel.setObjectName("sampleAreaLabel")
        self.sampleLayout.addWidget(self.sampleAreaLabel,1,2)
        
        self.sampleArea = ScientificDoubleSpinBox()
        self.sampleArea.setObjectName("sampleArea")
        self.sampleLayout.addWidget(self.sampleArea,1,3)
        
        self.sampleCommentLabel = QtWidgets.QLabel('Sample Comment:')
        self.sampleCommentLabel.setObjectName("sampleCommentLabel")
        self.sampleLayout.addWidget(self.sampleCommentLabel,2,0)
        
        self.sampleComment = QtWidgets.QLineEdit()
        self.sampleComment.setObjectName("sampleComment")
        self.sampleLayout.addWidget(self.sampleComment,2,1,1,3)
        
        # ROW 2 TEMPERATURE
        self.tempBox = QtWidgets.QGroupBox('Temperature Parameters')
        self.tempBox.setObjectName("tempBox")
        #self.tempBox.setFlat(True)
        self.buttonRow2.addWidget(self.tempBox)
        
        self.tempLayout = QtWidgets.QGridLayout()
        self.tempLayout.setObjectName("tempLayout")
        self.tempBox.setLayout(self.tempLayout)
        
        self.tempStartLabel = QtWidgets.QLabel('Initial Temperature (K):')
        self.tempStartLabel.setObjectName("tempStartLabel")
        self.tempLayout.addWidget(self.tempStartLabel,0,0)
        
        self.tempStart = ScientificDoubleSpinBox()
        self.tempStart.setObjectName("tempStart")
        self.tempLayout.addWidget(self.tempStart,0,1)

        self.tempEndLabel = QtWidgets.QLabel('Final Temperature (K):')
        self.tempEndLabel.setObjectName("tempEndLabel")
        self.tempLayout.addWidget(self.tempEndLabel,1,0)

        self.tempEnd = ScientificDoubleSpinBox()
        self.tempEnd.setObjectName("tempEnd")
        self.tempLayout.addWidget(self.tempEnd,1,1)

        self.tempStepLabel = QtWidgets.QLabel('Temperature Step (K):')
        self.tempStepLabel.setObjectName("tempStepLabel")
        self.tempLayout.addWidget(self.tempStepLabel,2,0)
        
        self.tempStep = ScientificDoubleSpinBox()
        self.tempStep.setObjectName("tempStep")
        self.tempLayout.addWidget(self.tempStep,2,1)

        self.tempIdleLabel = QtWidgets.QLabel('Idle Temperature (K):')
        self.tempIdleLabel.setObjectName("tempIdleLabel")
        self.tempLayout.addWidget(self.tempIdleLabel,3,0)
        
        self.tempIdle = ScientificDoubleSpinBox()
        self.tempIdle.setObjectName("tempIdle")
        self.tempLayout.addWidget(self.tempIdle,3,1)
        
        self.tempStableLabel = QtWidgets.QLabel('Temp. Stability (K):')
        self.tempStableLabel.setObjectName("tempStableLabel")
        self.tempLayout.addWidget(self.tempStableLabel,0,2)
        
        self.tempStable = ScientificDoubleSpinBox()
        self.tempStable.setObjectName("tempStable")
        self.tempLayout.addWidget(self.tempStable,0,3)
        
        self.timeStableLabel = QtWidgets.QLabel('Time Stability (s):')
        self.timeStableLabel.setObjectName("timeStableLabel")
        self.tempLayout.addWidget(self.timeStableLabel,1,2)
        
        self.timeStable = QtWidgets.QSpinBox()
        self.timeStable.setObjectName("timeStable")
        self.tempLayout.addWidget(self.timeStable,1,3)
        
        self.buttonIdle = QtWidgets.QPushButton()
        self.buttonIdle.setObjectName("buttonIdle")
        self.tempLayout.addWidget(self.buttonIdle,4,0,1,2)
    
        self.radioSampleLayout = QtWidgets.QHBoxLayout()
        self.radioSampleLayout.setObjectName("radioSampleLayout")
        self.tempLayout.addLayout(self.radioSampleLayout,2,3,1,1)
        
        self.radioSampleLabel = QtWidgets.QLabel('Sample Sensor:')
        self.radioSampleLabel.setObjectName("radioSampleLabel")
        self.tempLayout.addWidget(self.radioSampleLabel,2,2)
    
        self.radioSampleA = QtWidgets.QRadioButton('A')
        self.radioSampleA.setObjectName("radioSampleA")
        self.radioSampleLayout.addWidget(self.radioSampleA)
        
        self.radioSampleB = QtWidgets.QRadioButton('B')
        self.radioSampleB.setObjectName("radioSampleB")
        self.radioSampleLayout.addWidget(self.radioSampleB)
        
        self.radioSampleGroup = QtWidgets.QButtonGroup()
        self.radioSampleGroup.addButton(self.radioSampleA)
        self.radioSampleGroup.addButton(self.radioSampleB)
        
        self.radioControlLayout = QtWidgets.QHBoxLayout()
        self.radioControlLayout.setObjectName("radioControlLayout")
        self.tempLayout.addLayout(self.radioControlLayout,3,3,1,1)
        
        self.radioControlLabel = QtWidgets.QLabel('Control Sensor:')
        self.radioControlLabel.setObjectName("radioControlLabel")
        self.tempLayout.addWidget(self.radioControlLabel,3,2)
        
        self.radioControlA = QtWidgets.QRadioButton('A')
        self.radioControlA.setObjectName("radioControlA")
        self.radioControlLayout.addWidget(self.radioControlA)
        
        self.radioControlB = QtWidgets.QRadioButton('B')
        self.radioControlB.setObjectName("radioControlB")
        self.radioControlLayout.addWidget(self.radioControlB)
        
        self.radioControlGroup = QtWidgets.QButtonGroup()
        self.radioControlGroup.addButton(self.radioControlA)
        self.radioControlGroup.addButton(self.radioControlB)
        
        self.radioHeaterLayout = QtWidgets.QHBoxLayout()
        self.radioHeaterLayout.setObjectName("radioHeaterLayout")
        self.tempLayout.addLayout(self.radioHeaterLayout,4,2,1,2)
        
        self.radioHeaterLabel = QtWidgets.QLabel('Heater Range:\t')
        self.radioHeaterLabel.setObjectName("radioControlLabel")
        self.radioHeaterLayout.addWidget(self.radioHeaterLabel)
        
        self.radioHeaterLow = QtWidgets.QRadioButton('Low')
        self.radioHeaterLow.setObjectName("radioHeaterLow")
        self.radioHeaterLayout.addWidget(self.radioHeaterLow)
        
        self.radioHeaterMed = QtWidgets.QRadioButton('Med')
        self.radioHeaterMed.setObjectName("radioHeaterMed")
        self.radioHeaterLayout.addWidget(self.radioHeaterMed)
        
        self.radioHeaterHi = QtWidgets.QRadioButton('Hi')
        self.radioHeaterHi.setObjectName("radioHeaterHi")
        self.radioHeaterLayout.addWidget(self.radioHeaterHi)
        
        self.radioHeaterGroup = QtWidgets.QButtonGroup()
        self.radioHeaterGroup.addButton(self.radioHeaterLow)
        self.radioHeaterGroup.addButton(self.radioHeaterMed)
        self.radioHeaterGroup.addButton(self.radioHeaterHi)
        
        # ROW 3 DLTS
        self.dltsBox = QtWidgets.QGroupBox('DLTS Parameters')
        self.dltsBox.setObjectName("dltsBox")
        self.buttonRow3.addWidget(self.dltsBox)
        
        self.dltsLayout = QtWidgets.QGridLayout()
        self.dltsLayout.setObjectName("dltsLayout")
        self.dltsBox.setLayout(self.dltsLayout)
        
        self.dltsBiasLabel = QtWidgets.QLabel('Steady-state bias (V):')
        self.dltsBiasLabel.setObjectName("dltsBiasLabel")
        self.dltsLayout.addWidget(self.dltsBiasLabel,0,0)
        
        self.dltsBias = ScientificDoubleSpinBox()
        self.dltsBias.setObjectName("dltsBias")
        self.dltsLayout.addWidget(self.dltsBias,0,1)

        self.dltsPulseLabel = QtWidgets.QLabel('Pulse Height (V):')
        self.dltsPulseLabel.setObjectName("dltsPulseLabel")
        self.dltsLayout.addWidget(self.dltsPulseLabel,1,0)

        self.dltsPulse = ScientificDoubleSpinBox()
        self.dltsPulse.setObjectName("dltsPulse")
        self.dltsLayout.addWidget(self.dltsPulse,1,1)

        self.dltsPWidthLabel = QtWidgets.QLabel('Pulse Width (s):')
        self.dltsPWidthLabel.setObjectName("dltsPWidthLabel")
        self.dltsLayout.addWidget(self.dltsPWidthLabel,2,0)
        
        self.dltsPWidth = ScientificDoubleSpinBox()
        self.dltsPWidth.setObjectName("dltsPWidth")
        self.dltsLayout.addWidget(self.dltsPWidth,2,1)

        self.dltsTWidthLabel = QtWidgets.QLabel('Transient Width (s):')
        self.dltsTWidthLabel.setObjectName("dltsTWidthLabel")
        self.dltsLayout.addWidget(self.dltsTWidthLabel,0,2)
        
        self.dltsTWidth = ScientificDoubleSpinBox()
        self.dltsTWidth.setObjectName("dltsTWidth")
        self.dltsLayout.addWidget(self.dltsTWidth,0,3)
        
        self.dltsSampleLabel = QtWidgets.QLabel('Sampling Time (s):')
        self.dltsSampleLabel.setObjectName("dltsSampleLabel")
        self.dltsLayout.addWidget(self.dltsSampleLabel,1,2)
        
        self.dltsSample = QtWidgets.QSpinBox()
        self.dltsSample.setObjectName("dltsSample")
        self.dltsLayout.addWidget(self.dltsSample,1,3)
        
        # ROW 4 MFIA
        self.mfiaBox = QtWidgets.QGroupBox('MFIA Parameters')
        self.mfiaBox.setObjectName("mfiaBox")
        self.buttonRow4.addWidget(self.mfiaBox)
        
        self.mfiaLayout = QtWidgets.QGridLayout()
        self.mfiaLayout.setObjectName("mfiaLayout")
        self.mfiaBox.setLayout(self.mfiaLayout)
        
        self.mfiaSampleLabel = QtWidgets.QLabel('Sampling Rate (Hz):')
        self.mfiaSampleLabel.setObjectName("mfiaSampleLabel")
        self.mfiaLayout.addWidget(self.mfiaSampleLabel,0,0)
        
        self.mfiaSample = QtWidgets.QSpinBox()
        self.mfiaSample.setObjectName("mfiaSample")
        self.mfiaLayout.addWidget(self.mfiaSample,0,1)

        self.mfiaFreqLabel = QtWidgets.QLabel('AC Frequency (Hz):')
        self.mfiaFreqLabel.setObjectName("mfiaFreqLabel")
        self.mfiaLayout.addWidget(self.mfiaFreqLabel,1,0)

        self.mfiaFreq = QtWidgets.QSpinBox()
        self.mfiaFreq.setObjectName("mfiaFreq")
        self.mfiaLayout.addWidget(self.mfiaFreq,1,1)

        self.mfiaAmpLabel = QtWidgets.QLabel('AC Amplitude (V):')
        self.mfiaAmpLabel.setObjectName("mfiaAmpLabel")
        self.mfiaLayout.addWidget(self.mfiaAmpLabel,0,2)
        
        self.mfiaAmp = ScientificDoubleSpinBox()
        self.mfiaAmp.setObjectName("mfiaAmp")
        self.mfiaLayout.addWidget(self.mfiaAmp,0,3)

        self.mfiaTCLabel = QtWidgets.QLabel('Time Constant (s):')
        self.mfiaTCLabel.setObjectName("mfiaTCLabel")
        self.mfiaLayout.addWidget(self.mfiaTCLabel,1,2)
        
        self.mfiaTC = ScientificDoubleSpinBox()
        self.mfiaTC.setObjectName("mfiaTC")
        self.mfiaLayout.addWidget(self.mfiaTC,1,3)
        
        self.mfiaRangeLabel = QtWidgets.QLabel('Current Range (A):')
        self.mfiaRangeLabel.setObjectName("mfiaRangeLabel")
        self.mfiaLayout.addWidget(self.mfiaRangeLabel,2,0)
        
        self.mfiaRange = ScientificDoubleSpinBox()
        self.mfiaRange.setObjectName("mfiaRange")
        self.mfiaLayout.addWidget(self.mfiaRange,2,1)
        
        self.mfiaRejectLabel = QtWidgets.QLabel('Recovery Samples:')
        self.mfiaRejectLabel.setObjectName("mfiaRejectLabel")
        self.mfiaLayout.addWidget(self.mfiaRejectLabel,2,2)
        
        self.mfiaReject = QtWidgets.QSpinBox()
        self.mfiaReject.setObjectName("mfiaReject")
        self.mfiaLayout.addWidget(self.mfiaReject,2,3)

        # Row 5
        self.buttonInit = QtWidgets.QPushButton()
        self.buttonInit.setObjectName("buttonInit")
        self.buttonRow5.addWidget(self.buttonInit)
        
        self.buttonStart = QtWidgets.QPushButton()
        self.buttonStart.setObjectName("startDLTS")
        self.buttonRow5.addWidget(self.buttonStart)
        
        self.buttonStop = QtWidgets.QPushButton()
        self.buttonStop.setObjectName("stopDLTS")
        self.buttonRow5.addWidget(self.buttonStop)
        
        self.saveLog = QtWidgets.QPushButton()
        self.saveLog.setObjectName("saveLog")
        self.buttonRow5.addWidget(self.saveLog)

        # ROW 6
        #self.buttonClick = QtWidgets.QPushButton()
        #self.buttonClick.setObjectName("buttonClick")
        #self.buttonRow6.addWidget(self.buttonClick)
        
        #self.generateError = QtWidgets.QPushButton()
        #self.generateError.setObjectName("generateError")
        #self.buttonRow6.addWidget(self.generateError)
        
        #self.generatePlot = QtWidgets.QPushButton()
        #self.generatePlot.setObjectName("generatePlot")
        #self.buttonRow6.addWidget(self.generatePlot)

        #self.clearPlot = QtWidgets.QPushButton()
        #self.clearPlot.setObjectName("clearPlot")
        #self.buttonRow6.addWidget(self.clearPlot)

        
        ## GRAPH
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setObjectName("graphWidget")
        self.topLayout.addWidget(self.graphWidget)
        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Capacitance (pF)', **styles)
        self.graphWidget.setLabel('bottom', 'Sample Number', **styles)
        
        ## LOG WINDOW
        self.logWindow = QtWidgets.QPlainTextEdit()
        self.logWindow.setReadOnly(True)
        self.logWindow.setObjectName("logWindow")
        self.mainLayout.addWidget(self.logWindow)
        
        ## MENU AND STATUS BARS
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        # INITIALIZE VALUES
        self.retranslate_ui(MainWindow) # Initialize UI Labels
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.sampleMat.setText("GaAs")
        self.sampleArea.setValue(0.196)
        self.tempStart.setRange(0,1000)
        self.tempStart.setValue(300)
        self.tempEnd.setRange(0,1000)
        self.tempEnd.setValue(50)
        self.tempStep.setRange(0,100)
        self.tempStep.setValue(0.5)
        self.tempIdle.setRange(0,1000)
        self.tempIdle.setValue(200)
        self.tempStable.setRange(0,1000)
        self.tempStable.setValue(0.1)
        self.timeStable.setRange(0,1000)
        self.timeStable.setValue(5)
        self.radioSampleB.setChecked(1)
        self.radioControlB.setChecked(1)
        self.radioHeaterHi.setChecked(1)
        self.dltsBias.setRange(-10,10)
        self.dltsBias.setValue(-2.0)
        self.dltsPulse.setRange(-10,10)
        self.dltsPulse.setValue(1.8)
        self.dltsPWidth.setValue(0.002)
        self.dltsTWidth.setValue(0.150)
        self.dltsSample.setValue(15)
        self.mfiaSample.setMaximum(857144)
        self.mfiaSample.setValue(107143)
        self.mfiaFreq.setMaximum(5e6)
        self.mfiaFreq.setValue(1e6)
        self.mfiaAmp.setValue(0.125)
        self.mfiaTC.setValue(2.4e-6)
        self.mfiaSample.setGroupSeparatorShown(1)
        self.mfiaFreq.setGroupSeparatorShown(1)
        self.graphWidget.setBackground('w')
        self.state_pre()
        
        
        # UI SIGNALS->SLOTS
        #self.buttonClick.clicked.connect(self.button_click)
        #self.generateError.clicked.connect(self.generate_error)
        #self.generatePlot.clicked.connect(self.generate_plot)
        #self.clearPlot.clicked.connect(self.clear_plot)
        self.saveLog.clicked.connect(self.save_log)
        self.buttonInit.clicked.connect(self.state_inited)
        self.buttonStart.clicked.connect(self.state_started)
        self.buttonStop.clicked.connect(self.state_stopwait)
        self.logWindow.textChanged.connect(lambda: self.saveLog.setEnabled(1)) # lambda needed to allow custom slot here



    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mfiaDLTS2 Acquire"))
        self.buttonIdle.setText(_translate("MainWindow", "Go To Idle Temperature Now"))
        self.buttonInit.setText(_translate("MainWindow", "Initialize Hardware"))
        self.buttonStart.setText(_translate("MainWindow", "Start Scan"))
        self.buttonStop.setText(_translate("MainWindow", "Stop Scan"))
        #self.buttonClick.setText(_translate("MainWindow", "Clicky Button"))
        #self.generateError.setText(_translate("MainWindow", "Generate Error"))
        #self.generatePlot.setText(_translate("MainWindow", "Generate Plot"))
        #self.clearPlot.setText(_translate("MainWindow", "Clear Plot"))
        self.saveLog.setText(_translate("MainWindow", "Save Log"))


        
    def generate_dateTime(self):
        dateTime = QDateTime.currentDateTime().toString("yy.MM.dd-hh:mm:ss")
        return "[" + dateTime + "] "

    def generate_log(self,string,color="black"):
        timeText = self.generate_dateTime()
        logText = timeText + "<font color=\"" + color + "\">" + string + "</font>"
        self.logWindow.appendHtml(logText)

    #def button_click(self):
    #    self.generate_log("Button clicked!")
                
   # def generate_error(self):
    #    self.generate_log("Error: Fake error","red")
        
    #def generate_plot(self):
    #    nPlots = 100
    #    nSamples = 500
    #    curves = []
    #    data = np.random.normal(size=(nPlots*23,nSamples))
    #    for idx in range(nPlots):
    #        curve = pg.PlotCurveItem(pen=(170-idx,nPlots*4))  #7->17 out of 40
    #        self.graphWidget.addItem(curve)
    #        #curve.setPos(0,idx*6)
    #        curves.append(curve)
    #        curves[idx].setData(data[(idx)%data.shape[0]])
            
    #    self.generate_log("Data plotted")
        
    #def clear_plot(self):
    #    self.graphWidget.clear()
    #    self.generate_log("Plot data deleted")
        
    def save_log(self):
        self.generate_log("Saving Log...","blue")
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Log File Save","","Log File (*.log)", options=options)
        if fileName:
            file = open(fileName, 'w')
            text = self.logWindow.toPlainText()
            file.write(text)
            file.close()  
            self.generate_log("Log Saved","green") 
        else:
            self.generate_log("Save canceled","orange") 


    ## DEFINE THE UI MACHINE STATES    
    def state_pre(self):
        self.saveLog.setEnabled(0)
        self.buttonIdle.setEnabled(0)
        self.buttonStart.setEnabled(0)
        self.buttonStop.setEnabled(0)
        #self.buttonStop.hide()
        
    def state_inited(self):
        _translate = QtCore.QCoreApplication.translate
        self.buttonInit.setText(_translate("MainWindow", "Re-Initialize Hardware"))
        self.buttonStart.setEnabled(1)
        self.buttonIdle.setEnabled(1)
        
    def state_started(self):
        self.buttonInit.setEnabled(0)
        self.buttonIdle.setEnabled(0)
        self.buttonStart.setEnabled(0)
        #self.buttonStart.hide()
        self.buttonStop.setEnabled(1)
        #self.buttonStop.show()

    def state_stopwait(self):
        self.buttonStop.setEnabled(0)
                
    def state_stopped(self):
        self.buttonInit.setEnabled(1)
        self.buttonStart.setEnabled(0)
        self.buttonIdle.setEnabled(1)
