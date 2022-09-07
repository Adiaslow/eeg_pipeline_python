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

