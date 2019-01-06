import json
import numpy as np
import pandas as pd


from length import Length
from tolerance import Tolerance


class DataJson:

    def __init__(self, ctx, date):
        self.ctx = ctx
        self.coils = self.read_data_json(date)
        # print(self.coils)

    def get_json_path(self, date):
        return "{}/{}/{}/{}".format(
            self.ctx.cfg["export_dir"],
            self.ctx.line,
            date[:6],
            "ExportedData_{}_{}.json".format(
                self.ctx.line,
                date
            )
        )

    def read_data_json(self, date):
        print(self.get_json_path(date))
        coils = {}
        with open(self.get_json_path(date), "r") as json_file:
            coils = json.load(json_file)
        return coils

    def get_coil_id_list(self):
        return self.coils.keys()

    def get_start_end(self, segment, hdtl):
        head_len = hdtl.get_head_len()
        tail_len = hdtl.get_tail_len()
        head_cut = hdtl.get_head_cut()
        tail_cut = hdtl.get_tail_cut()

        # start 正数 end 倒数
        start = 0
        end = 0
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
        return start, end

    def get_result(self, start, end, fn_tag, tol):
        array = self.data[start:end]
        if fn_tag == "aimrate":
            result = self.calc_aimrate(array, tol)
        elif fn_tag == "max":
            result = np.max(array)
        elif fn_tag == "min":
            result = np.min(array)
        elif fn_tag == "std":
            result = np.std(array)
        elif fn_tag == "mean":
            result = np.mean(array)
        else:
            raise Exception("wrong stat func input")
        return result

    def calc_aimrate(self, array, tol):
        upper = tol.get_upper()
        lower = tol.get_lower()
        return pd.Series(array).apply(
            lambda x: 1 if (x >= lower) & (x <= upper) else 0).mean() * 100

    def calc(self, rule, id_record):
        factor = rule["FACTOR"]
        fn_tag = rule["STAT_FN"]
        segment = rule["SEGMENT"]
        hdtl = Length(self.ctx, rule, id_record)
        tol = Tolerance(rule, id_record)

        coil_id = id_record["coil_id"]
        self.data = self.coils[coil_id]["factors"][factor]["data"]
        start, end = self.get_start_end(segment, hdtl)
        result = self.get_result(start, end, fn_tag, tol)
        return result
