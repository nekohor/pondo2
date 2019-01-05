import subprocess
import numpy as np


class Exe():
    def __init__(self):
        self.raw_cmd = "C:/Windows/pondex.exe"

    def set_signals(self, signals):
        self.signals = signals

    def set_dcapath(self, dcapath):
        self.dca_path = dcapath

    def set_stat_fn(self, stat_fn):
        self.stat_name = stat_fn

    def set_segment(self, segment):
        self.seg_name = segment

    def set_length(self, hdtl):
        self.head_len = hdtl.get_head_len()
        self.tail_len = hdtl.get_tail_len()
        self.head_cut = hdtl.get_head_cut()
        self.tail_cut = hdtl.get_tail_cut()

    def set_upper_lower(self, tolerance):
        self.upper = tolerance.get_upper()
        self.lower = tolerance.get_lower()

    def execute(self):
        self.argv = []
        self.argv.append(self.raw_cmd)
        self.argv.append(self.dca_path)
        self.argv.extend(self.signals)
        self.argv.extend([self.stat_name, self.seg_name])
        self.argv.extend([
            str(self.head_len),
            str(self.tail_len),
            str(self.head_cut),
            str(self.tail_cut)
        ])
        self.argv.extend([str(self.upper), str(self.lower)])
        self.cmd = " ".join(self.argv)
        # print(self.cmd)
        self.p = subprocess.Popen(
            self.cmd, shell=True, stdout=subprocess.PIPE).stdout

        self.p = subprocess.Popen(
            self.cmd,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = self.p.communicate()
        try:
            self.calc_result = float(out)
        except Exception as e:
            print(out, "the subprocess returns nan data")
            self.calc_result = np.nan
        return self.calc_result
