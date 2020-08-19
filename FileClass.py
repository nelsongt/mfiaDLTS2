# Copyright George Nelson 2020
# FileClass, worker object that saves files

import datetime
import os

from LogClass import LogObject


class FileSave(LogObject):
    def __init__(self,sample):
        super(FileSave, self).__init__()
        self.transient = []
        self.now = datetime.datetime.now()
        path = os.path.abspath(os.path.dirname(__file__))
        self.save_folder = []

    def TRANSIENT_FILE(self,sample,dlts,mfia,currentNum,setTemperature,avgTemperature):
        #TransientFile Saves transient data to LDLTS compatible iso file

    #     fileName = strcat(sample.name,'_',num2str(currentNum),'_',num2str(setTemperature),'.iso');
        fileName = ''.join((sample.name,'_',num2str(currentNum),'_',num2str(setTemperature),'.iso'))
    #     fileDate = datestr(now,'dd-mm-yyyy  HH:MM');
        fileNow = datetime.datetime.now()
        fileDate = fileNow.strftime("%d-%m-%Y %H:%M")
    

    #     status = mkdir(strcat(pwd,'\',sample.save_folder));
        self.save_folder = os.path.join(path,'Data',''.join((sample.name,'_',self.now.strftime("%d-%m-%Y %H:%M"))))
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
    #     fid = fopen(fullfile(strcat(pwd,'\',sample.save_folder),fileName),'wt');
        fid = open(os.path.join(self.save_folder,fileName,'wt'))
    #     fprintf(fid, '[general]\n');
        fid.write('[general]\n')
    #     fprintf(fid, 'software=mfiaDLTS v1.0\n');  %TODO: check if compat. w/ LDLTS software
        fid.write('software=mfiaDLTS v2.0\n') #TODO check if working w/ LDLTS software
    #     fprintf(fid, 'hardware=MFIA\n');
        fid.write('hardware=MFIA\n')
    #     fprintf(fid, 'serial number=000 [000000000]\n');
        fid.write('serial number=000 [000000000]\n')
    #     fprintf(fid, 'user=%s\n', sample.user);
        fid.write('user={}\n'.format(sample.user))
    #     fprintf(fid, 'type=LapDLTS\n');
        fid.write('type=LapDLTS\n')
    #     fprintf(fid, 'source=Laplace DLTS experiment\n');
        fid.write('source=Laplace DLTS experiment\n')
    #     fprintf(fid, 'date=%s\n', fileDate);
        fid.write('date={}\n'.format(fileDate))
    #     fprintf(fid, 'data base=C:\\Path\\To\\Database.mdb\n');
        fid.write('data base=C:\\Path\\To\\Database.mdb\n')
    #     fprintf(fid, 'data name=%s\n', fileName);
        fid.write('data name={}\n'.format(fileName))
    #     fprintf(fid, 'comment=%s\n', sample.comment);
        fid.write('comment={}\n'.format(sample.comment))
    #     fprintf(fid, '[sample]\n');
        fid.write('[sample]\n')
    #     fprintf(fid, 'Material=%s\n', sample.material);
        fid.write('Material={}\n'.format(sample.material))
    #     fprintf(fid, 'Identifier=%s\n', sample.name);
        fid.write('Identifier={}\n'.format(sample.name))
    #     fprintf(fid, 'area= %s\n', sample.area);
        fid.write('area= {}\n'.format(sample.area))
    #     fprintf(fid, 'effective mass= .041\n');  %TODO
        fid.write('effective mass= .041\n') #TODO
    #     fprintf(fid, 'dielectric constant= 13.9\n');  %TODO
        fid.write('dielectric constant= 13.9\n')  #TODO
    #     fprintf(fid, 'No Bias Capacitance= 130\n');  %TODO
        fid.write('No Bias Capacitance= 130\n')  #TODO
    #     fprintf(fid, 'Bias Capacitance= 68.12258\n');  %TODO
        fid.write('Bias Capacitance= 68.12258\n')  #TODO
    #     fprintf(fid, '[capacitance meter]\n');
        fid.write('[capacitance meter]\n')
    #     fprintf(fid, 'range= 300\n');  %TODO
        fid.write('range= 300\n')  #TODO
    #     fprintf(fid, '[generator]\n');
        fid.write('[generator]\n')
    #     fprintf(fid, 'bias=%.3f\n', mfia.ss_bias);
        fid.write('bias={:.3f}\n'.format(dlts.ss_bias))
    #     fprintf(fid, '1st Pulse Bias=%.3f\n', mfia.ss_bias+mfia.pulse_height);
        fid.write('1st Pulse Bias={:.3f}\n'.format(dlts.ss_bias+dlts.pulse_height))
    #     fprintf(fid, '2nd Pulse Bias=0\n');
        fid.write('2nd Pulse Bias=0\n')
    #     fprintf(fid, 'Injection Pulse Bias=0\n');
        fid.write('Injection Pulse Bias=0\n')
    #     fprintf(fid, '1st Pulse Width=%f\n', mfia.pulse_width);
        fid.write('1st Pulse Width={:f}\n'.format(dlts.pulse_width))
    #     fprintf(fid, '2nd Pulse Width=0.0\n');
        fid.write('2nd Pulse Width=0.0\n')
    #     fprintf(fid, 'Injection Pulse Width=0.0\n');
        fid.write('Injection Pulse Width=0.0\n')
    #     fprintf(fid, '2nd pulse=off\n');
        fid.write('2nd pulse=off\n')
    #     fprintf(fid, '2nd pulse interlacing= 10\n');
        fid.write('2nd pulse interlacing= 10\n')
    #     fprintf(fid, 'Injection pulse=off\n');
        fid.write('Injection pulse=off\n')
    #     fprintf(fid, 'Like Pulse1=on\n');
        fid.write('Like Pulse1=on\n')
    #     fprintf(fid, 'Extra delay added=off\n');
        fid.write('Extra delay added=off\n')
    #     fprintf(fid, 'Extra Delay Value= .001\n');
        fid.write('Extra Delay Value= .001\n')
    #     fprintf(fid, '[acquisition]\n');
        fid.write('[acquisition]\n')
    #     fprintf(fid, 'first sample= 0\n');
        fid.write('first sample= 0\n')
    #     fprintf(fid, 'last sample= %d\n', length(transient)-1);
        fid.write('last sample= {:d}\n'.format(len(self.transient)-1))
    #     fprintf(fid, 'Sampling Rate= %d\n', mfia.sample_rate);
        fid.write('Sampling Rate= {:d}\n'.format(mfia.sample_rate))
    #     fprintf(fid, 'No samples= %d\n', length(transient));
        fid.write('No samples= %d\n'.format(len(self.transient)))
    #     fprintf(fid, 'No scans= 150\n');
        fid.write('No scans= 150\n')  #TODO
    #     fprintf(fid, 'gain= 1\n');
        fid.write('gain= 1\n')
    #     fprintf(fid, '[parameters]\n');
        fid.write('[parameters]\n')
    #     fprintf(fid, 'Sampling Rate= %d\n', mfia.sample_rate);
        fid.write('Sampling Rate= {:d}\n'.format(mfia.sample_rate))
    #     fprintf(fid, 'capacitance meter range= 300\n');
        fid.write('capacitance meter range= 300\n')  #TODO
    #     fprintf(fid, 'bias=%.3f\n', mfia.ss_bias);
        fid.write('bias={:.3f}\n'.format(dlts.ss_bias))
    #     fprintf(fid, '1st Pulse Bias=%.3f\n', mfia.ss_bias+mfia.pulse_height);
        fid.write('1st Pulse Bias={:.3f}\n'.format(dlts.ss_bias+dlts.pulse_height))
    #     fprintf(fid, '2nd Pulse Bias=0\n');
        fid.write('2nd Pulse Bias=0\n')
    #     fprintf(fid, 'Injection Pulse Bias=0\n');
        fid.write('Injection Pulse Bias=0\n')
    #     fprintf(fid, '1st Pulse Width=%f\n', mfia.pulse_width);
        fid.write('1st Pulse Width={:f}\n'.format(dlts.pulse_width))
    #     fprintf(fid, '2nd Pulse Width=0.0\n');
        fid.write('2nd Pulse Width=0.0\n')
    #     fprintf(fid, 'Injection Pulse Width=0.0\n');
        fid.write('Injection Pulse Width=0.0\n')
    #     fprintf(fid, 'Extra Delay Value= .001\n');
        fid.write('Extra Delay Value= .001\n')  #TODO
    #     fprintf(fid, 'No samples= %d\n', length(transient));
        fid.write('No samples= {:d}\n'.format(len(self.transient)))
    #     fprintf(fid, 'No scans= 150\n');  %TODO
        fid.write('No scans= 150\n')  #TODO
    #     fprintf(fid, 'gain= 1\n');
        fid.write('gain= 1\n')
    #     fprintf(fid, 'Bias Capacitance= 68.12258\n');  %TODO
        fid.write('Bias Capacitance= 68.12258\n')  #TODO
    #     fprintf(fid, 'CurrentTransient=off\n');
        fid.write('CurrentTransient=off\n')
    #     fprintf(fid, 'temperature= %f\n', avgTemperature);
        fid.write('temperature= {:f}\n'.format(avgTemperature))
    #     fprintf(fid, 'temperatureSet= %d\n', setTemperature);
        fid.write('temperatureSet= {:d}\n'.format(setTemperature))
    #     fprintf(fid, 'magnetic field= 0\n');
        fid.write('magnetic field= 0\n')
    #     fprintf(fid, 'pressure= 0\n');
        fid.write('pressure= 0\n')
    #     fprintf(fid, 'illumination= 0\n');
        fid.write('illumination= 0\n')
    #     fprintf(fid, '[noise]\n');
        fid.write('[noise]\n')
    #     fprintf(fid, 'level= 2.049163E-02\n');  %TODO
        fid.write('level= 2.049163E-02\n')  #TODO
    #     fprintf(fid, '\n');
        fid.write('\n')
    #     fprintf(fid, '[data]\n');
        fid.write('[data]\n')
    #     for i=1:length(transient)
    #         fprintf(fid, ' %f \n', transient(i)');
    #     end
        for i in range(len(self.transient)):
            fid.write(' {:f} \n',format(self.transient[i]))
    #     fclose(fid);
        fid.close()

