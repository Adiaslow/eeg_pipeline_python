# !/usr/bin/python3.10

import header as h

if __name__ == "__main__":
    input_file = "MUAD205062022EOFull.xdf"
    eeg = h.file_input.read_xdf(input_file)