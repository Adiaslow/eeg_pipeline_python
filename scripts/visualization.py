import header as h

def plot_time_series(eeg, window_size, start_time):
    time_series = eeg.signal
    channels = eeg.channels
    channel_count = eeg.channel_count
    effective_srate = eeg.effective_srate

    fig, ax = h.plt.subplots(figsize=(16,9))

    window_size = 8
    window = window_size * (effective_srate + start_time)

    for i in range(0, channel_count):
        ax.plot([0, window], [50*i, 50*i], c="gray", lw=0.8, alpha=0.25)
        ax.plot(time_series.iloc[i, 0:window] + 50 * i, lw=0.8, alpha=1)
        ax.annotate(channels[i].label, xy=(-window_size * 5, 50 * i - 5))

    ax.xaxis.set_ticks(h.np.arange(0, window, effective_srate))
    ax.grid(True, which='both', axis='both')
    ax.set_ylabel("dB")
    ax.set_xlabel("Time (miliseconds)")

    ax.get_yaxis().set_visible(False)
    h.plt.tight_layout()

    h.plt.show()