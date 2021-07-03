# Copyright George Nelson 2020
# Parameter class, generates data structs for hardware parameters


class SampleParams(object):
    __slots__ = ['user', 'name', 'material', 'area', 'comment']

    #def __init__(self):

class DLTSParams(object):
    __slots__ = ['ss_bias', 'pulse_height', 'trns_length', 'pulse_width', 'sample_time']

    #def __init__(self):

class TempParams(object):
    __slots__ = ['temp_init', 'temp_step', 'temp_final', 'temp_idle', 'temp_stability', 'time_stability']

    #def __init__(self):
    
class LakeshoreParams(object):
    __slots__ = ['control', 'sample', 'heatpower']

    #def __init__(self):

class MFIAParams(object):
    __slots__ = ['sample_rate', 'ac_freq', 'ac_ampl', 'time_constant']

    #def __init__(self):
