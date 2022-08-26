class eeg:
    def __init__(self,name, type, channel_count, nominal_srate, channel_format, manufacturer,
                 model, precision, compensated_lag, reference_label, subtracted, common_average,
                 stream_id, effective_srate):

        self.name = name
        self.type = type
        self.channel_count = channel_count
        self.nominal_srate = nominal_srate
        self.channel_format = channel_format
        self.manufacturer = manufacturer
        self.model = model
        self.precision = precision
        self.compensated_lag = compensated_lag
        self.reference_label = reference_label
        self.subtracted = subtracted
        self.common_average = common_average
        self.model = stream_id
        self.effective_srate = effective_srate

"""class channel:
    def __init__(self):"""
