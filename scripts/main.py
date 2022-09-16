# !/usr/bin/python3.10

import header as h

if __name__ == "__main__":
    input_file = "MUAD205062022EOFull.xdf"
    eeg = h.file_input.read_xdf(input_file)
    # wavelet_transform = h.transforms.haar_wavelet_transform(eeg, True, 1)
    fft = h.transforms.fast_fourier_transform(eeg)
    # h.visualization.plot_time_series(eeg, 8, 0)