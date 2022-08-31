# !/usr/bin/python3.10

import header as h


def read_xdf(input_file):
    """Reads XDF output from Neurofield EEG"""

    # Load the XDF file
    xdf = h.pyxdf.load_xdf(input_file)[0][0]

    # Top level dict of the XDF
    info = xdf["info"]

    # Data in the "info" dict
    name = info["name"][0]
    type = info["type"][0]
    channel_count = int(info["channel_count"][0])
    nominal_srate = int(info["nominal_srate"][0])
    channel_format = info["channel_format"][0]
    stream_id = info["stream_id"]
    effective_srate = int(info["effective_srate"])

    # Secondary dict of the "info" dict
    desc = info["desc"][0]

    # Secondary dict of the "desc" dict
    channels_dict = desc["channels"][0]
    channels_list = channels_dict["channel"]

    channels = []

    for i in range(0, channel_count):
        channel = channels_list[i]

        label = channel["label"][0]

        location = channel["location"][0]
        x = float(location["X"][0])
        y = float(location["Y"][0])
        z = float(location["Z"][0])

        location = h.classes.Location(x, y, z)

        unit = channel["unit"][0]

        channel = h.classes.Channel(label, location, unit)

        channels.append(channel)

    # Secondary dict of the "desc" dict
    acquisition = desc["acquisition"][0]

    # Data in the "acquisition" dict
    manufacturer = acquisition["manufacturer"][0]
    model = acquisition["model"][0]
    precision = acquisition["precision"][0]
    compensated_lag = acquisition["compensated_lag"][0]

    # Secondary dict of the "desc" dict
    reference = desc["reference"][0]

    # Data in the "reference" dict
    reference_label = reference["label"][0]
    subtracted = reference["subtracted"][0]
    common_average = reference["common_average"][0]

    # Signal
    channel_labels = []
    time_series = []

    for i in range(0, channel_count):
        channel_label = channels[i].label
        full_time_series = xdf["time_series"].T
        channel_labels.append(channel_label)
        time_series.append(full_time_series[i])

    time_series = h.np.array(time_series)

    signal = h.pd.DataFrame(time_series, index=channel_labels)

    print(f"\n{signal}")
    print(f"\nChannels = {channel_count}")
    print(f"Effective Sample Rate= {effective_srate}")

    # Initialize EEG class with the data from the XDF
    eeg = h.classes.Eeg(name, type, channel_count, nominal_srate, channel_format, manufacturer,
                        model, precision, compensated_lag, reference_label, subtracted,
                        common_average, stream_id, effective_srate, channels, signal)

    # print(f"Channel {eeg.channels[0].label}'s \"X\" value is {eeg.channels[0].location.x}")

    return eeg
