import header as h

def haar_wavelet_transform(eeg):
    y = eeg.signal.iloc[0, :100]
    print()
    print(y)

    channels = eeg.channels
    channel_count = eeg.channel_count
    effective_srate = eeg.effective_srate

    v = h.np.array(1 / h.np.sqrt(2), 1 / h.np.sqrt(2))
    w = h.np.array(1 / h.np.sqrt(2), - 1 / h.np.sqrt(2))

    sums = []
    diffs = []

    for i in range(0, len(y) - 1, 2):
        sums.append((1/h.np.sqrt(2)) * y[i] + (1/h.np.sqrt(2)) * y[i + 1])
        diffs.append((1/h.np.sqrt(2)) * y[i] - (1/h.np.sqrt(2)) * y[i + 1])

    threshold = 1
    for d in range(0, len(diffs)):
        if diffs[d] < threshold and diffs[d] > -threshold:
            diffs[d] = 0

    sums_and_diffs = [*sums, *diffs]

    new_y = []

    for j in range(0, len(sums) - 1, 1):
        new_y.append((sums[j] + diffs[j]) / 2)
        new_y.append((sums[j] - diffs[j]) / 2)
        # print(str(sums[j]) + " " + str(diffs[j]))


    print()
    print()
    print("Len of Sums = " + str(len(sums)))
    print("Len of Diffs = " + str(len(diffs)))
    print("Len of Sums and Diffs = " + str(len(sums_and_diffs)))
    print("Len of y = " + str(len(y)))
    print("Len of New y = " + str(len(new_y)))

    h.plt.plot(y - h.np.mean(y), lw=1)
    h.plt.plot(new_y - h.np.mean(new_y), lw=1)
    h.plt.tight_layout()
    h.plt.show()

    pass

def continuous_wavelet_transform():
    pass

