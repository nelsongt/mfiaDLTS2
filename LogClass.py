# Copyright George Nelson 2020

from PyQt5.QtCore import QObject,pyqtSignal

class LogObject(QObject):
    log_signal = pyqtSignal(str,str)
    finished = pyqtSignal()

    def __init__(self):
        super(LogObject, self).__init__()

    def generate_log(self,string,color="black"):
        self.log_signal.emit(string,color)