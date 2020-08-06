# Copyright George Nelson 2020
# Lakeshore class, generates instances of Lakeshore virtual interface

import lakeshore
import time

from LogClass import LogObject


class Lakeshore(LogObject):

    def __init__(self):
        super(Lakeshore, self).__init__()
        #self.getCurrentTemp = []
        #self.getCurrentWait = []
        #self.unstable = False

        # Stopped state when user clicks stop
        self.stopped = []

    def reset(self):
        self.generate_log("Initializing Lakeshore...","blue")
        self.stopped = False
        #     getCurrentTemp = sampleSpaceTemperature
        #self.getCurrentTemp = 290
        #self.getCurrentWait = 2
        #self.unstable = False

        # Check for lakeshore 331
        if self.isLakeshoreInstalled() == 0:
            self.generate_log("Lakeshore Not Found. Connect and re-initialize.","orange")
            return False


    #     % Setup Lakeshore
    #     response = lakeshoreQuery('CSET?');
    #     if ~strcmp(response,'B,1,0,2')
    #         lakeshoreQuery('CSET 1,B,1,0,2');   % Control loop 1, sensor B, in Kelvin (1), default heater off (0), heater units power (2)
    #     end
    #     response = lakeshoreQuery('RANGE?');
    #     if ~strcmp(response,'3')
    #         lakeshoreQuery('RANGE 3');          % Set heater to high (3), medium (2), low (1)
    #     end
    #     if strcmp(response,'-1')
    #         cprintf('red','Error configuring lakeshore. Exiting...\n');
    #         success = false;
    #     end
        self.generate_log("Lakeshore configure OK.","Green")
        return True
    #     cprintf('green','Lakeshore configure OK.\n');
    #     success = true;
    #     end
    #
    def isLakeshoreInstalled(self):
        # Initialize communication to temperature controller.
        try:
            obj1 = lakeshore.Model335(9600)
        except:
            return 0
        #if not obj1:
        #    return 0

        #try:
        #    obj1 = rm.open_resource('GPIB0::12::INSTR')
        #except:
        #    return 0


        #     obj1 = instrfind('Type', 'gpib', 'BoardIndex', 0, 'PrimaryAddress', 12);

    #     % Create the GPIB object if it does not exist
    #     % otherwise use the object that was found.
    #     if isempty(obj1)
    #         obj1 = gpib('NI', 0, 12);
    #     else
    #         fclose(obj1);
    #         obj1 = obj1(1);
    #     end
    #
    #     installed = 0;
    #
    #     try
    #     fopen(obj1)
    #     fprintf(obj1, '*idn?');
    #     pause(.05);
    #
    #     cut = 1:10;
    #     idnCheck = 'LSCI,MODEL330,0,032301';
    #     idn = fscanf(obj1);
    #
    #     if strcmp(idn(cut),idnCheck(cut))
    #         installed = 1;
    #     else
    #         installed = 0;
    #     end
    #
    #     catch err
    #         disp('Cannot connect to Lakeshore 335!')
    #         disp(err.message)
    #         installed = 0;
    #     end
    #     % Close communication.
    #     fclose(obj1)
    #     end
    #
    #

    # def lakeshoreQuery(self,commmand):

        # % Initialize communication to temperature controller.
        # obj1 = instrfind('Type', 'gpib', 'BoardIndex', 0, 'PrimaryAddress', 12);
        # % Create the GPIB object if it does not exist
        # % otherwise use the object that was found.
        # if isempty(obj1)
        #     obj1 = gpib('NI', 0, 12);
        # else
        #     fclose(obj1);
        #     obj1 = obj1(1);
        # end
        #
        # % Get the temperature
        # try
        #     fopen(obj1);
        #     response = sn(query(obj1,commmand));
        #
        #     % Close communication.
        #     fclose(obj1);
        # catch err
        #     err
        #     disp(err.message)
        #     response = '-1';
        # end
        # end
        #
        # % Snip out certain characters
        # function x =sn(x)
        # x(x==10)=[];
        # x(x==13)=[];
        # end

    # def sampleSpaceTemperature(self,varargin):
    #
    #     % Initialize communication to temperature controller.
    #     obj1 = instrfind('Type', 'gpib', 'BoardIndex', 0, 'PrimaryAddress', 12);
    #     % Create the GPIB object if it does not exist
    #     % otherwise use the object that was found.
    #     if isempty(obj1)
    #         obj1 = gpib('NI', 0, 12);
    #     else
    #         fclose(obj1);
    #         obj1 = obj1(1);
    #     end
    #
    #     % Get the temperature
    #     fopen(obj1)
    #
    #     tempString = sn(query(obj1,'KRDG? B'));
    #
    #     if nargin&&strcmpi(varargin{1},'string')
    #         temp = tempString;
    #     else
    #         temp = str2double(tempString);
    #     end
    #
    #     % Close communication.
    #     fclose(obj1)
    #     end
    #
    #     % Snip out certain characters
    #     function x =sn(x)
    #     x(x==10)=[];
    #     x(x==13)=[];

    def SET_TEMP(self,setPoint,tempStable,timeStable):
    #     lakeshoreQuery(strcat('SETP ',num2str(setPoint)))  # Set point to lakeshore
    #     getCurrentTemp = sampleSpaceTemperature
        getCurrentTemp = 290
        getCurrentWait = timeStable
        unstable = False
        while (abs(getCurrentTemp - setPoint) > tempStable or getCurrentWait >= 0) and self.stopped == False:  # Continuously loop the time and temp stability until both are met
            while abs(getCurrentTemp - setPoint) > tempStable and self.stopped == False:
                time.sleep(2)  # Wait for temperature to reach set point
    #           getCurrentTemp = sampleSpaceTemperature #TODO
                getCurrentTemp = setPoint
                self.generate_log("Current Temp: {:3.2f}. Set point: {:3.2f}. Delta: {:2.2f}.".format(getCurrentTemp,setPoint,getCurrentTemp-setPoint),"blue")
            unstable = False;
            while getCurrentWait >= 0 and unstable == False and self.stopped == False:
                self.generate_log("Wait for time stability: {:d} s left.".format(getCurrentWait),"blue")
                time.sleep(1)                          # Wait 1 second
                getCurrentWait = getCurrentWait - 1          # Subtract one from our counter
                #getCurrentTemp = sampleSpaceTemperature #TODO
                if abs(getCurrentTemp - setPoint) > tempStable:  # check again for temp stability, if not stable then flag for restart
                    unstable = True

            if unstable == True:  # check again for temp stability, if not stable then restart process
                getCurrentWait = timeStable
    #             cprintf([0.9100 0.4100 0.1700],'Temperature not time stable (refine PID?), restarting stability process...\n');
                self.generate_log("Temperature not time stable (refine PID?), restarting stability process...","black") #TODO color [0.9100 0.4100 0.1700]
        if self.stopped == False:
            self.generate_log("Temperature has stabilized!","green")