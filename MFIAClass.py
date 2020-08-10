# Copyright George Nelson 2020
# MFIAclass, generates instances of MFIA virtual interfaces

import time
import numpy
import zhinst.utils

from LogClass import LogObject


## Replicate MATLAB tic/toc functions, copied from user Benben on stackoverflow
def TicTocGenerator():
    # Generator that returns time differences
    ti = 0           # initial time
    tf = time.time() # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf-ti # returns the time difference

TicToc = TicTocGenerator() # create an instance of the TicTocGen generator

# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    if tempBool:
        print( "Elapsed time: %f seconds.\n" %tempTimeInterval )

def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)

TicToc2 = TicTocGenerator() # create another instance of the TicTocGen generator

def toc2(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc2
    tempTimeInterval = next(TicToc2)
    if tempBool:
        print( "Elapsed time 2: %f seconds.\n" %tempTimeInterval )

def tic2():
    # Records a time in TicToc2, marks the beginning of a time interval
    toc2(False)
## End tic/toc function


class MFIA(LogObject):
    def __init__(self):
        super(MFIA, self).__init__()
        self.data = []
        self.device = []
        self.ziDAQ = []

    def reset(self,dlts,mfia):
        self.generate_log("Initializing MFIA...","blue")


        ## Open connection to the ziServer (socket for sync interface)
        self.ziDAQ = ziPython.ziDAQServer('127.0.0.1',8004,6)  # Use local data server for best performance
        # Get device name automagically (e.g. 'dev234')
        self.device = self.autoDetect(ziDAQ)
        # or specify manually
        #device = 'dev3327'


        # Enable IA module
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/enable", device), 1);
    #     ziDAQ('setInt', ['/' device '/imps/0/enable'], 1);
    #
    #
        vrange = 10;
        irange = 0.0001;
        phase_offset = 0;

        # Setup IA module
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/mode", device), 1)
        self.ziDAQ.setInt(String.Format("/{0}/system/impedance/filter", device), 1);
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/model", device), 0);
    #     ziDAQ('setInt', ['/' device '/imps/0/mode'], 1);
    #     ziDAQ('setInt', ['/' device '/system/impedance/filter'], 1);
    #     ziDAQ('setInt', ['/' device '/imps/0/model'], 0);
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/auto/output", device), 0)
        self.ziDAQ.setInt(String.Format("/{0}/system/impedance/precision", device), 0)
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/maxbandwidth", device), 1000)
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/omegasuppression", device), 60)
    #     ziDAQ('setInt', ['/' device '/imps/0/auto/output'], 0);
    #     ziDAQ('setInt', ['/' device '/system/impedance/precision'], 0);
    #     ziDAQ('setDouble', ['/' device '/imps/0/maxbandwidth'], 1000);
    #     ziDAQ('setDouble', ['/' device '/imps/0/omegasuppression'], 60);
    #
        # Input settings, set to current and set range
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/auto/inputrange", device), 0)
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/current/range", device), irange)
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/voltage/range", device), vrange)
    #     ziDAQ('setInt', ['/' device '/imps/0/auto/inputrange'], 0);
    #     ziDAQ('setDouble', ['/' device '/imps/0/current/range'], irange);
    #     %ziDAQ('setDouble', ['/' device '/imps/0/voltage/range'], vrange);
    #
        # Lock in params & filtering
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/demod/sinc", device), 1)
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/demod/order", device), 8)
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/auto/bw", device), 0)
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/phaseshift", device), phase_offset)
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/timeconstant", device), mfia.time_constant)
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/harmonic", device), 1)
    #     ziDAQ('setInt', ['/' device '/imps/0/demod/sinc'], 1);
    #     ziDAQ('setInt', ['/' device '/imps/0/demod/order'], 8);
    #     ziDAQ('setInt', ['/' device '/imps/0/auto/bw'], 0);
    #     ziDAQ('setDouble', ['/' device '/demods/0/phaseshift'], phase_offset);
    #     ziDAQ('setDouble', ['/' device '/imps/0/demod/timeconstant'], mfia.time_constant);
    #     ziDAQ('setDouble', ['/' device '/imps/0/demod/harmonic'], 1);
    #
        # Oscillator settings
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/freq", device), mfia.ac_freq)
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/output/amplitude", device), mfia.ac_ampl)
    #     ziDAQ('setDouble', ['/' device '/imps/0/freq'], mfia.ac_freq);
    #     ziDAQ('setDouble', ['/' device '/imps/0/output/amplitude'], mfia.ac_ampl);
    #
        # Output settings
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/output/range", device), vrange)
        self.ziDAQ.setInt(String.Format("/{0}/imps/0/output/on", device), 1)
        if dlts.pulse_height:
            self.ziDAQ.setInt(String.Format("/{0}/sigouts/0/add", device), 1)
        else:
            self.ziDAQ.setInt(String.Format("/{0}/sigouts/0/add", device), 0)
    #     ziDAQ('setDouble', ['/' device '/imps/0/output/range'], vrange);
    #     ziDAQ('setInt', ['/' device '/imps/0/output/on'], 1);
    #     if mfia.pulse_height  % Check if a pulse bias is set, if so add to ss bias
    #         ziDAQ('setInt', ['/' device '/sigouts/0/add'], 1);
    #     else
    #         ziDAQ('setInt', ['/' device '/sigouts/0/add'], 0);
    #     end
        self.ziDAQ.setDouble(String.Format("/{0}/sigouts/0/offset", device), dlts.ss_bias)
        self.ziDAQ.setInt(String.Format("/{0}/tu/thresholds/0/input", device), 59)
        self.ziDAQ.setInt(String.Format("/{0}/tu/thresholds/1/input", device), 59)
        self.ziDAQ.setInt(String.Format("/{0}/tu/thresholds/0/inputchannel", device), 0)
        self.ziDAQ.setInt(String.Format("/{0}/tu/thresholds/1/inputchannel", device), 0)
        self.ziDAQ.setInt(String.Format("/{0}/tu/logicunits/0/inputs/0/not", device), 1)
        self.ziDAQ.setInt(String.Format("/{0}/tu/logicunits/1/inputs/0/not", device), 1)
    #     ziDAQ('setDouble', ['/' device '/sigouts/0/offset'], dlts.ss_bias);
    #     ziDAQ('setInt', ['/' device '/tu/thresholds/0/input'], 59);
    #     ziDAQ('setInt', ['/' device '/tu/thresholds/1/input'], 59);
    #     ziDAQ('setInt', ['/' device '/tu/thresholds/0/inputchannel'], 0);
    #     ziDAQ('setInt', ['/' device '/tu/thresholds/1/inputchannel'], 0);
    #     ziDAQ('setInt', ['/' device '/tu/logicunits/0/inputs/0/not'], 1);
    #     ziDAQ('setInt', ['/' device '/tu/logicunits/1/inputs/0/not'], 1);
        self.ziDAQ.setDouble(String.Format("/{0}/tu/thresholds/0/deactivationtime", device), dlts.trns_length+0.001)
        self.ziDAQ.setDouble(String.Format("/{0}/tu/thresholds/0/activationtime", device), dlts.pulse_width)
        self.ziDAQ.setDouble(String.Format("/{0}/tu/thresholds/1/deactivationtime", device), 0)
        self.ziDAQ.setDouble(String.Format("/{0}/tu/thresholds/1/activationtime", device), 0)
    #     ziDAQ('setDouble', ['/' device '/tu/thresholds/0/deactivationtime'], dlts.trns_length+0.001); #add 1ms buffer time
    #     ziDAQ('setDouble', ['/' device '/tu/thresholds/0/activationtime'], dlts.pulse_width);
    #     ziDAQ('setDouble', ['/' device '/tu/thresholds/1/deactivationtime'], 0);
    #     ziDAQ('setDouble', ['/' device '/tu/thresholds/1/activationtime'], 0);
        self.ziDAQ.setInt(String.Format("/{0}/auxouts/0/outputselect", device), 13)
        self.ziDAQ.setInt(String.Format("/{0}/auxouts/1/outputselect", device), 13)
        self.ziDAQ.setInt(String.Format("/{0}/auxouts/0/demodselect", device), 0)
        self.ziDAQ.setInt(String.Format("/{0}/auxouts/1/demodselect", device), 1)
    #     ziDAQ('setInt', ['/' device '/auxouts/0/outputselect'], 13);
    #     ziDAQ('setInt', ['/' device '/auxouts/1/outputselect'], 13);
    #     ziDAQ('setInt', ['/' device '/auxouts/0/demodselect'], 0);
    #     ziDAQ('setInt', ['/' device '/auxouts/1/demodselect'], 1);
        self.ziDAQ.setDouble(String.Format("/{0}/auxouts/0/scale", device), dlts.pulse_height)
        self.ziDAQ.setDouble(String.Format("/{0}/auxouts/0/offset", device), 0)
        self.ziDAQ.setDouble(String.Format("/{0}/auxouts/1/scale", device), -5.0)
        self.ziDAQ.setDouble(String.Format("/{0}/auxouts/1/offset", device), 5.0)
    #     ziDAQ('setDouble', ['/' device '/auxouts/0/scale'], dlts.pulse_height);
    #     ziDAQ('setDouble', ['/' device '/auxouts/0/offset'], 0);
    #     ziDAQ('setDouble', ['/' device '/auxouts/1/scale'], -5.0);
    #     ziDAQ('setDouble', ['/' device '/auxouts/1/offset'], 5.0);
    #
        # Data stream settings
        self.ziDAQ.setDouble(String.Format("/{0}/imps/0/demod/rate", device), mfia.sample_rate)
    #     ziDAQ('setDouble', ['/' device '/imps/0/demod/rate'], mfia.sample_rate);


    # def autoDetect(self,device):
    #     nodes = lower(ziDAQ('listNodes','/'));
    #     dutIndex = strmatch('dev', nodes);
    #     if length(dutIndex) > 1
    #         error('autoDetect does only support a single MFIA configuration.');
    #     elseif isempty(dutIndex)
    #         error('No DUT found. Make sure that the USB cable is connected to the host and the device is turned on.');
    #     end
    #     % Found only one device -> selection valid.
    #     device = lower(nodes{dutIndex});
    #     fprintf('Initialized MFIA %s ...\n', device)
    #     end

    def MFIA_CAPACITANCE_DAQ(self,deviceId,dlts,mfia):


        # if ~exist('deviceId', 'var')
        #     error(['No value for device_id specified. The first argument to the ' ...
        #         'example should be the device ID on which to run the example, ' ...
        #         'e.g. ''dev3327'''])
        # end

        # Unsubscribe from any streaming data
        #self.ziDAQ('unsubscribe', '*');
        #  Flush all the buffers.
        self.ziDAQ.sync()

        # Create a Data Acquisition Module instance, the return argument is a handle to the module.
        h = self.ziDAQ.dataAcquisitionModule()

        ## Configure the Data Acquisition Module
        # Device on which trigger will be performed
        #sample_rate = ziDAQ('getDouble', ['/' deviceId '/imps/0/demod/rate']);
        sample_rate = self.ziDaq.getDouble('/%s/imps/0/demod/rate' %deviceId)
        trigger_count = ceil(0.9*mfia.sample_time/mfia.trns_length)
        sample_count = sample_rate*mfia.trns_length
        # ziDAQ('set', h, 'dataAcquisitionModule/device', deviceId)
        h.set('device', deviceId)
        # ziDAQ('set', h, 'dataAcquisitionModule/count', trigger_count);
        h.set('count', trigger_count)
        # ziDAQ('set', h, 'dataAcquisitionModule/endless', 0);
        h.set('endless', 0)
        # ziDAQ('set', h, 'dataAcquisitionModule/grid/mode', 4);
        h.set('grid/mode', 4)
        # ziDAQ('set', h, 'dataAcquisitionModule/type', 6);
        h.set('type', 6)
        # ziDAQ('set', h, 'dataAcquisitionModule/triggernode', ['/' deviceId '/demods/0/sample.trigin1']);
        h.set('triggernode', '/%s/demods/0/sample.trigin1' %deviceId)
        # %   edge:
        # %     POS_EDGE = 1
        # %     NEG_EDGE = 2
        # %     BOTH_EDGE = 3
        # ziDAQ('set', h, 'dataAcquisitionModule/edge', 2)
        h.set('edge', 2)
        # ziDAQ('set', h, 'dataAcquisitionModule/grid/cols', sample_count);
        h.set('grid/cols', sample_count)
        # ziDAQ('set', h, 'dataAcquisitionModule/grid/rows', 1);
        h.set('grid/rows', 1)
        # ziDAQ('set', h, 'dataAcquisitionModule/holdoff/time', 0.0);
        h.set('holdoff/time', 0.0)
        # ziDAQ('set', h, 'dataAcquisitionModule/delay', 0.0);
        h.set('delay', 0.0)

        ## Subscribe to the demodulators
        # Subscribe to the 0th IA module
        # ziDAQ('subscribe', h, ['/' deviceId '/imps/0/sample.param1']);
        h.subscribe('/%s/imps/0/sample.param1' %deviceId)


        # %% Start recording
        # % now start the thread -> ready to be triggered
        # ziDAQ('execute', h);
        h.execute()

        timeout = 1.3*mfia.sample_time # [s]
        total_triggers = 0
        sampleCap = []
        tic()
        tic2()
        dt_read = 2.1
        transferNotFinished = not bool(self.ziDAQ.finished())
        while transferNotFinished and toc() < timeout:
            time.sleep(0.05)
            # Perform an intermediate readout of the data. the data between reads is
            # not acculmulated in the module - it is cleared, so that the next time
            # you do a read you (should) only get the triggers that came inbetween the
            # two reads.
            if toc2() > dt_read:
                data = self.ziDAQ.read()
                #if ziCheckPathInData(data, ['/' deviceId '/imps/0/sample_param1'])
                if data.deviceId.imps(1).sample_param1:
                    loop_triggers = len(data.deviceId.imps(1).sample_param1)
                    total_triggers = total_triggers + loop_triggers
                    # save data, using some idea of mine that might save CPU time
                    capData = []
                    for i in loop_triggers:
                        #capData.append(data.deviceId.imps(1).sample_param1{1,i}.value)
                        capData = data
                        #timeStamp = []; %TODO
                    sampleCap.append(capData)
                #cprintf('blue','Acquired %d of total %d transients: %.1f%% (elapsed time %.3f s)\n', total_triggers, trigger_count, 100*ziDAQ('progress', h),toc(t0));
                tRead = tic2()
                transferNotFinished = not h.finished()

        # Timeout check
        if toc() > timeout:
        # If for some reason we're not obtaining triggers quickly enough, the
        # following command will force the end of the recording.
            if total_triggers == 0:
                h.finish()
                h.clear()
                #error('Trigger failure before timeout (%d seconds). Missing feedback cable between sigout 2 and trigin 1?', timeout);
            #else:
                #cprintf('systemcommands','Warning: Only acquired %d transients. Operation timed out (%.2f s) before acquiring %d transients.\n', total_triggers, timeout, trigger_count);
        #else:
            #cprintf('green','Done.\n');

        h.unsubscribe('/%s/imps/0/sample.param1' %deviceId)
        h.clear()

        return sampleCap


    def MFIA_TRANSIENT_AVERAGER_DAQ(self,capArray,mfia):
        SR = mfia.sample_rate
        capArray_pF = capArray*1e12
        transients = len(capArray_pF,1)
        numSamples = len(capArray_pF,2)  #length of transient in data points
        rejectSamples = 4 #ength of hardware recovery in data points, generally first 80-100 usec of data if using George's suggested MFIA settings
        realNumSamp = numSamples - rejectSamples
        times = numpy.linspace(1/SR,(1/SR)*realNumSamp,realNumSamp)

        sum = numpy.zeros(realNumSamp,transients-1);
        int_i = 1+rejectSamples;
        int_f = numSamples;
        for z in transients-1:   #TODO first transient is always lead by NaN?
            transient = capArray_pF[z+1,int_i:int_f]
            #plot(time,transient,'Color',color(z,:))
            #hold on
            sum[:,z] = transient

        averagedTransient = numpy.nanmean(sum)
        return averagedTransient

        # Transient averaging & plotting
        # close all
        # figure('Position',[200,500,500,375]);
        # hold on;
        # color = summer(transients);

        #
        #
        # xlabel('Time (s)','fontsize',20);
        # ylabel('Capacitance (pF)','fontsize',20);
        # title('Average transient','fontsize',28);
        #
        # % Overlap the averaged tranisent
        # averagedTransient = nanmean(sum.');
        # plot(time,averagedTransient,'r');
        # hold off;
        #
        # % Semilog plot
        # figure('Position',[700,500,500,375]);
        # hold on;
        # semilogx(averagedTransient);
        # set(gca, 'XScale', 'log','xlim',[1 realNumSamp]);
        # ax1 = gca;
        # ax1_pos = ax1.Position;
        # ax1.XLabel.String = 'Samples';
        # ax1.YLabel.String = 'Capacitance (pF)';
        # pos=get(gca,'position');  % retrieve the current values
        # pos(4)=0.95*pos(4);       % try reducing height 5%
        # set(gca,'position',pos);  % write the new values
        # ax2 = axes('Position',ax1.Position,...
        #     'XAxisLocation','top',...
        #     'YAxisLocation','right',...
        #     'xlim',[1/SR (1/SR)*realNumSamp],...
        #     'XScale','log',...
        #     'Color','none',...
        #     'ytick',[]);
        # ax2.XLabel.String = 'Time (s)';
        # hold off;
        # end