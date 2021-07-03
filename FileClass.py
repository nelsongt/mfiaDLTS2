# Copyright George Nelson 2021
# FileClass, worker object that saves files

import datetime
import os

from LogClass import LogObject


class FileSave(LogObject):
    def __init__(self):
        super(FileSave, self).__init__()
        self.transient = []
        now = datetime.datetime.now()
        self.nowString = now.strftime("%d-%m-%Y-%H-%M-%S")
        self.path = os.path.abspath(os.path.dirname(__file__))
        self.save_folder = []

    def TRANSIENT_FILE(self,sample,dlts,mfia,currentNum,setTemperature,avgTemperature):
        #TransientFile Saves transient data to LDLTS compatible iso file

        fileName = ''.join((sample.name,'_',str(currentNum),'_',str(setTemperature),'.iso'))
        fileNow = datetime.datetime.now()
        fileDate = fileNow.strftime("%d-%m-%Y %H:%M")


    #     status = mkdir(strcat(pwd,'\',sample.save_folder));
        self.save_folder = os.path.join(self.path,'Data',''.join((sample.name,'_',self.nowString)))
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
        fid = open(os.path.join(self.save_folder,fileName),'wt')
        fid.write('[general]\n')
        fid.write('software=mfiaDLTS v2.0\n') #TODO check if working w/ LDLTS software
        fid.write('hardware=MFIA\n')
        fid.write('serial number=000 [000000000]\n')
        fid.write('user={}\n'.format(sample.user))
        fid.write('type=LapDLTS\n')
        fid.write('source=Laplace DLTS experiment\n')
        fid.write('date={}\n'.format(fileDate))
        fid.write('data base=C:\\Path\\To\\Database.mdb\n')
        fid.write('data name={}\n'.format(fileName))
        fid.write('comment={}\n'.format(sample.comment))
        fid.write('[sample]\n');
        fid.write('Material={}\n'.format(sample.material))
        fid.write('Identifier={}\n'.format(sample.name))
        fid.write('area= {}\n'.format(sample.area))
        fid.write('effective mass= .041\n') #TODO
        fid.write('dielectric constant= 13.9\n')  #TODO
        fid.write('No Bias Capacitance= 130\n')  #TODO
        fid.write('Bias Capacitance= 68.12258\n')  #TODO
        fid.write('[capacitance meter]\n')
        fid.write('range= 300\n')  #TODO
        fid.write('[generator]\n')
        fid.write('bias={:.3f}\n'.format(dlts.ss_bias))
        fid.write('1st Pulse Bias={:.3f}\n'.format(dlts.ss_bias+dlts.pulse_height))
        fid.write('2nd Pulse Bias=0\n')
        fid.write('Injection Pulse Bias=0\n')
        fid.write('1st Pulse Width={:f}\n'.format(dlts.pulse_width))
        fid.write('2nd Pulse Width=0.0\n')
        fid.write('Injection Pulse Width=0.0\n')
        fid.write('2nd pulse=off\n')
        fid.write('2nd pulse interlacing= 10\n')
        fid.write('Injection pulse=off\n')
        fid.write('Like Pulse1=on\n')
        fid.write('Extra delay added=off\n')
        fid.write('Extra Delay Value= .001\n')
        fid.write('[acquisition]\n')
        fid.write('first sample= 0\n')
        fid.write('last sample= {:d}\n'.format(len(self.transient)-1))
        fid.write('Sampling Rate= {:d}\n'.format(mfia.sample_rate))
        fid.write('No samples= {:d}\n'.format(len(self.transient)))
        fid.write('No scans= 150\n')  #TODO
        fid.write('gain= 1\n')
        fid.write('[parameters]\n')
        fid.write('Sampling Rate= {:d}\n'.format(mfia.sample_rate))
        fid.write('capacitance meter range= 300\n')  #TODO
        fid.write('bias={:.3f}\n'.format(dlts.ss_bias))
        fid.write('1st Pulse Bias={:.3f}\n'.format(dlts.ss_bias+dlts.pulse_height))
        fid.write('2nd Pulse Bias=0\n')
        fid.write('Injection Pulse Bias=0\n')
        fid.write('1st Pulse Width={:f}\n'.format(dlts.pulse_width))
        fid.write('2nd Pulse Width=0.0\n')
        fid.write('Injection Pulse Width=0.0\n')
        fid.write('Extra Delay Value= .001\n')  #TODO
        fid.write('No samples= {:d}\n'.format(len(self.transient)))
        fid.write('No scans= 150\n')  #TODO
        fid.write('gain= 1\n')
        fid.write('Bias Capacitance= 68.12258\n')  #TODO
        fid.write('CurrentTransient=off\n')
        fid.write('temperature= {:f}\n'.format(avgTemperature))
        fid.write('temperatureSet= {:f}\n'.format(setTemperature))
        fid.write('magnetic field= 0\n')
        fid.write('pressure= 0\n')
        fid.write('illumination= 0\n')
        fid.write('[noise]\n')
        fid.write('level= 2.049163E-02\n')  #TODO
        fid.write('\n')
        fid.write('[data]\n')
        for i in range(len(self.transient)):
            fid.write(' {:f} \n'.format(self.transient[i]))
        fid.close()

