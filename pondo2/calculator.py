import numpy as np
import pandas as pd

from headtail import HeadTail
from tolerance import Tolerance


class Calculator():

    def __init__(self, ctx, coil_id, rule):
        self.ctx = ctx
        self.coil_id = coil_id
        self.rule = rule  # Rule

        self.data = self.ctx.coils.get_data(
            self.coil_id, self.rule.get_factor())

    def get_start_end(self):

        hdtl = HeadTail(self.ctx, self.coil_id, self.rule)
        head_len = hdtl.get_head_len()
        tail_len = hdtl.get_tail_len()
        head_cut = hdtl.get_head_cut()
        tail_cut = hdtl.get_tail_cut()

        # start 正数 end 倒数
        start = 0
        end = 0

        segment = self.rule.get_segment()
        num = len(self.data)

        if segment == "head":
            start = head_cut
            end = head_len + head_cut
        elif segment == "tail":
            start = num - tail_len - tail_cut
            end = num - tail_cut
        elif segment == "body":
            start = head_len + head_cut
            end = num - tail_len - tail_cut
        elif segment == "cdr":
            start = head_len + head_cut
            end = num - tail_cut
        elif segment == "main":
            start = head_cut
            end = num - tail_cut
        elif segment == "total":
            start = 0
            end = num
        elif segment == "first":
            start = head_cut
            end = head_cut + 5
        else:
            raise Exception("wrong segment input")
        return int(start), int(end)

    def get_result(self):

        start, end = self.get_start_end()
        array = self.data[start:end]

        if array.shape[0] == 0:
            return np.nan

        func_tag = self.rule.get_func_tag()
        if func_tag == "aimrate":
            result = self.calc_aimrate(array)
        elif func_tag == "stability":
            result = self.calc_stability(array)
        elif func_tag == "max":
            result = np.max(array)
        elif func_tag == "absmax":
            result = np.max(np.abs(array))
        elif func_tag == "min":
            result = np.min(array)
        elif func_tag == "std":
            result = np.std(array)
        elif func_tag == "mean":
            result = np.mean(array)
        elif func_tag == "absmean":
            result = np.mean(np.abs(array))
        else:
            raise Exception("wrong stat func input")
        return round(result, 4)

    def calc_aimrate(self, array):
        tol = Tolerance(self.ctx, self.coil_id, self.rule)
        upper = tol.get_upper()
        lower = tol.get_lower()
        return array.apply(
            lambda x: 1 if (x >= lower) & (x <= upper) else 0).mean() * 100

    def calc_stability(self, array):
        tol = self.rule.get_tol()
        aim = np.mean(array)
        upper = aim + tol
        lower = aim - tol
        return array.apply(
            lambda x: 1 if (x >= lower) & (x <= upper) else 0).mean() * 100

    def calc(self):
        result = self.get_result()
        return result

    def get_all(self):
        return self.data
