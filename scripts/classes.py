import header as h


class Eeg:
    def __init__(self,name, type, channel_count, nominal_srate, channel_format, manufacturer,
                 model, precision, compensated_lag, reference_label, subtracted, common_average,
                 stream_id, effective_srate, channels, signal):

        self.name = name # String
        self.type = type # String
        self.channel_count = channel_count # Int
        self.nominal_srate = nominal_srate # Int
        self.channel_format = channel_format # String
        self.manufacturer = manufacturer # String
        self.model = model # String
        self.precision = precision # Int
        self.compensated_lag = compensated_lag # Int
        self.reference_label = reference_label # String
        self.subtracted = subtracted # Bool
        self.common_average = common_average # Bool
        self.model = stream_id # String
        self.effective_srate = effective_srate # Int

        self.channels = channels # List
        self.signal = signal # Pandas Dataframe


class Channel:
    def __init__(self, label, location, unit):
        self.label = label # String
        self.location = location # Object
        self.unit = unit # String


class Location:
    def __init__(self, x, y, z):
        self.x = x # Float
        self.y = y # Float
        self.z = z # Float
