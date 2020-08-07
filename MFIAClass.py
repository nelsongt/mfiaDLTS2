# Copyright George Nelson 2020
# MFIAclass, generates instances of MFIA virtual interfaces

import zhinst.utils

from LogClass import LogObject


class MFIA(LogObject):
    def __init__(self):
        super(MFIA, self).__init__()
        self.data = []
        self.device = []
        self.ziDAQ = []

    def reset(self,dlts,mfia):
        self.generate_log("Initializing MFIA...","blue")
        
    
        ## Open connection to the ziServer (socket for sync interface)
        self.ziDAQ = ziPython.ziDAQServer('127.0.0.1',8004,6);    % Use local data server for best performance
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

    def MFIA_CAPACITANCE_DAQ(self,deviceId,mfia):
        
        #
        # if ~exist('deviceId', 'var')
        #     error(['No value for device_id specified. The first argument to the ' ...
        #         'example should be the device ID on which to run the example, ' ...
        #         'e.g. ''dev3327'''])
        # end
        #
        # % Unsubscribe from any streaming data
        # ziDAQ('unsubscribe', '*');
        # % Flush all the buffers.
        # ziDAQ('sync');
        #
        # % Create a Data Acquisition Module instance, the return argument is a handle to the module.
        # h = ziDAQ('dataAcquisitionModule');
        #
        # %% Configure the Data Acquisition Module
        # % Device on which trigger will be performed
        # sample_rate = ziDAQ('getDouble', ['/' deviceId '/imps/0/demod/rate']);
        # trigger_count = ceil(0.9*mfia.sample_time/mfia.trns_length);
        # sample_count = sample_rate*mfia.trns_length;
        # ziDAQ('set', h, 'dataAcquisitionModule/device', deviceId)
        # ziDAQ('set', h, 'dataAcquisitionModule/count', trigger_count);
        # ziDAQ('set', h, 'dataAcquisitionModule/endless', 0);
        # ziDAQ('set', h, 'dataAcquisitionModule/grid/mode', 4);
        # ziDAQ('set', h, 'dataAcquisitionModule/type', 6);
        # ziDAQ('set', h, 'dataAcquisitionModule/triggernode', ['/' deviceId '/demods/0/sample.trigin1']);
        # %   edge:
        # %     POS_EDGE = 1
        # %     NEG_EDGE = 2
        # %     BOTH_EDGE = 3
        # ziDAQ('set', h, 'dataAcquisitionModule/edge', 2)
        # ziDAQ('set', h, 'dataAcquisitionModule/grid/cols', sample_count);
        # ziDAQ('set', h, 'dataAcquisitionModule/grid/rows', 1);
        # ziDAQ('set', h, 'dataAcquisitionModule/holdoff/time', 0.0);
        # ziDAQ('set', h, 'dataAcquisitionModule/delay', 0.0);
        #
        # %% Subscribe to the demodulators
        # % Subscribe to the 0th IA module
        # ziDAQ('subscribe', h, ['/' deviceId '/imps/0/sample.param1']);
        #
        #
        # %% Start recording
        # % now start the thread -> ready to be triggered
        # ziDAQ('execute', h);
        #
        # timeout = 1.3*mfia.sample_time; % [s]
        # total_triggers = 0;
        # sampleCap = [];
        # t0 = tic;
        # tRead = tic;
        # dt_read = 2.1;
        # transferNotFinished = ~ziDAQ('finished', h);
        # while transferNotFinished && toc(t0) < timeout
        #     pause(0.05);
        #     % Perform an intermediate readout of the data. the data between reads is
        #     % not acculmulated in the module - it is cleared, so that the next time
        #     % you do a read you (should) only get the triggers that came inbetween the
        #     % two reads.
        #     if toc(tRead) > dt_read
        #         data = ziDAQ('read', h);
        #         if ziCheckPathInData(data, ['/' deviceId '/imps/0/sample_param1'])
        #             loop_triggers = length(data.(deviceId).imps(1).sample_param1);
        #             total_triggers = total_triggers + loop_triggers;
        #             % save data, using some idea of mine that might save CPU time
        #             capData = [];
        #             for i = 1:loop_triggers
        #                 capData = [capData; data.(deviceId).imps(1).sample_param1{1,i}.value];
        #                 timeStamp = []; %TODO
        #             end
        #             sampleCap = [sampleCap; capData];
        #         end
        #         cprintf('blue','Acquired %d of total %d transients: %.1f%% (elapsed time %.3f s)\n', total_triggers, trigger_count, 100*ziDAQ('progress', h),toc(t0));
        #         tRead = tic;
        #         transferNotFinished = ~ziDAQ('finished', h);
        #     end
        # end
        # % Timeout check
        # if toc(t0) > timeout
        # % If for some reason we're not obtaining triggers quickly enough, the
        # % following command will force the end of the recording.
        # if total_triggers == 0
        #     ziDAQ('finish', h);
        #     ziDAQ('clear', h);
        #     error('Trigger failure before timeout (%d seconds). Missing feedback cable between sigout 2 and trigin 1?', timeout);
        # else
        #     cprintf('systemcommands','Warning: Only acquired %d transients. Operation timed out (%.2f s) before acquiring %d transients.\n', total_triggers, timeout, trigger_count);
        # end
        # else
        #     cprintf('green','Done.\n');
        # end
        #
        # ziDAQ('unsubscribe', h, ['/' deviceId '/imps/0/sample'])
        # ziDAQ('clear', h);
        #
        # end

    # def MFIA_TRANSIENT_AVERAGER_DAQ(self,capArray,mfia):
        # %capArray = sampleCap;
        # %SR = sample_rate;
        # %TrnsLength = sample_period-pulse_width;
        # %   By George Nelson, Oct 2019
        #
        # SR = mfia.sample_rate;
        # capArray_pF = capArray*1e12;
        # transients = size(capArray_pF,1);
        # numSamples = size(capArray_pF,2);  %length of transient in data points
        # rejectSamples = 4;  %length of hardware recovery in data points, generally first 80-100 usec of data if using George's suggested MFIA settings
        # realNumSamp = numSamples - rejectSamples;
        # time = linspace(1/SR,(1/SR)*realNumSamp,realNumSamp);
        #
        #
        #
        # % Transient averaging & plotting
        # close all
        # figure('Position',[200,500,500,375]);
        # hold on;
        # color = summer(transients);
        # sum = zeros(realNumSamp,transients-1);
        # int_i = 1+rejectSamples;
        # int_f = numSamples;
        # for z = 1:transients-1   % TODO first transient is always lead by NaN?
        #     transient = capArray_pF(z+1,int_i:int_f);
        #     plot(time,transient,'Color',color(z,:))
        #     hold on
        #     sum(:,z) = transient;
        # end
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