# !/usr/bin/python3.10

import header as h

def read_xdf(input_file):
    """Reads XDF output from Neurofield EEG"""

    xdf = h.pyxdf.load_xdf(input_file)[0][0]

    info = xdf["info"]
    print(info)

    name = info["name"][0]
    type = info["type"][0]
    channel_count = info["channel_count"][0]
    nominal_srate = info["nominal_srate"][0]
    channel_format = info["channel_format"][0]

    desc = info["desc"][0]
    channels = desc["channels"][0]

    acquisition = desc["acquisition"][0]

    manufacturer = acquisition["manufacturer"][0]
    model = acquisition["model"][0]
    precision = acquisition["precision"][0]
    compensated_lag = acquisition["compensated_lag"][0]

    reference = desc["reference"][0]

    reference_label = reference["label"][0]
    subtracted = reference["subtracted"][0]
    common_average = reference["common_average"][0]

    stream_id = info["stream_id"]
    effective_srate = info["effective_srate"]

    eeg = h.classes.eeg(name, type, channel_count, nominal_srate, channel_format, manufacturer,
                        model, precision, compensated_lag, reference_label, subtracted, common_average,
                        stream_id, effective_srate)

    print(eeg)
