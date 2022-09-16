import header as h

def haar_wavelet_transform(eeg, energy_conserving, denoising_threshold):

    window_size = 256
    channels = eeg.channels
    channel_count = eeg.channel_count
    effective_srate = eeg.effective_srate

    y = eeg.signal.iloc[0, 0:window_size]

    sums = []
    diffs = []

    for i in range(0, (len(y) - 1), 2):
        sums.append((1/h.np.sqrt(2)) * y[i] + (1/h.np.sqrt(2)) * y[i + 1])
        diffs.append((1/h.np.sqrt(2)) * y[i] - (1/h.np.sqrt(2)) * y[i + 1])

    for d in range(0, len(diffs)):
        if diffs[d] < denoising_threshold and diffs[d] > - denoising_threshold:
            diffs[d] = 0

    sums_and_diffs = [*sums, *diffs]

    new_y = []

    if energy_conserving:
        for j in range(0, len(sums), 1):
            new_y.append((sums[j] + diffs[j]) / h.np.sqrt(2))
            new_y.append((sums[j] - diffs[j]) / h.np.sqrt(2))
    else:
        for j in range(0, len(sums), 1):
            new_y.append((sums[j] + diffs[j]) / 2)
            new_y.append((sums[j] - diffs[j]) / 2)

    print()
    print("Len of Sums = " + str(len(sums)))
    print("Len of Diffs = " + str(len(diffs)))
    print("Len of Sums and Diffs = " + str(len(sums_and_diffs)))
    print("Len of y = " + str(len(y)))
    print("Len of New y = " + str(len(new_y)))

    x = h.np.arange(0,window_size)
    h.plt.plot(y - h.np.mean(y) + 50, lw=1, color='black', alpha = 0.5)
    h.plt.plot(new_y - h.np.mean(new_y) + 50, lw=1, color='red', alpha = 0.5)
    h.plt.fill_between(x, y - h.np.mean(y) + 50, new_y - h.np.mean(new_y) + 50,
                       alpha=0.5)

    h.plt.tight_layout()
    h.plt.show()

def continuous_wavelet_transform():
    pass


def FFT(x):
    N = len(x)

    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = \
            h.np.exp(-2j * h.np.pi * h.np.arange(N) / N)

        X = h.np.concatenate( \
            [X_even + factor[:int(N / 2)] * X_odd,
             X_even + factor[int(N / 2):] * X_odd])
        return X


def fast_fourier_transform(eeg):

    window_size = 32
    channels = eeg.channels
    channel_count = eeg.channel_count
    effective_srate = eeg.effective_srate

    window = effective_srate * window_size

    h.plt.figure(figsize=(12, 6))

    for i in range(0, channel_count):
        x = list(eeg.signal.iloc[i, 0:window])

        X = FFT(x)

        # calculate the frequency
        N = len(X)
        n = h.np.arange(N)
        T = N/effective_srate
        freq = n/T


        """
        h.plt.subplot(121)
        h.plt.stem(freq, abs(X), 'b', markerfmt=" ", basefmt="-b")
        h.plt.xlabel('Freq (Hz)')
        h.plt.ylabel('FFT Amplitude |X(freq)|')
        """

        # Get the one-sided specturm
        n_oneside = N//2
        # get the one side frequency
        f_oneside = freq[:n_oneside]

        # normalize the amplitude
        X_oneside = X[:n_oneside]/n_oneside

        scaleing = 10

        X_ = X_oneside

        X_ = h.gaussian_filter1d(X_oneside, scaleing)

        # h.plt.subplot(122)
        h.plt.plot(f_oneside, abs(X_) * scaleing, lw=0.8)

    h.plt.xlabel('Freq (Hz)')
    h.plt.ylabel('Normalized FFT Amplitude |X(freq)|')
    h.plt.minorticks_on()
    h.plt.grid(which='both')
    h.plt.ylim((0,10))
    h.plt.xlim((0,40))
    h.plt.tight_layout()
    h.plt.show()
