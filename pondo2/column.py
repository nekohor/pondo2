import numpy as np


class Column():

    def __init__(self, rule):
        self.rule = rule

    def get_simple_col(self):
        return "_".join([
            self.rule["SEGMENT"],
            self.rule["FACTOR"],
            self.rule["STAT_FN"]])

    def get_col(self):
        col = self.get_simple_col()
        if self.rule["STAT_FN"].upper() == "AIMRATE":
            col = col + "_" + self.get_tolerance_tag()
        else:
            pass
        return col.upper()

    def get_tolerance_tag(self):
        if np.isnan(self.rule["LOWER"]) | np.isnan(self.rule["UPPER"]):
            return self.get_limit_tag()
        else:
            lower_tag = self.cut_to_int("{}".format(self.rule["LOWER"]))
            upper_tag = self.cut_to_int("{}".format(self.rule["UPPER"]))
            return lower_tag + "_" + upper_tag

    def get_limit_tag(self):
        if np.isnan(self.rule["TOL_PERC"]):
            return self.get_absolute_tag()
        else:
            return self.get_perc_tag()

    def get_absolute_tag(self):
        tol_tag = "{}".format(self.rule["TOL"] * self.mm_to_um())
        return self.cut_to_int(tol_tag)

    def get_perc_tag(self):
        tol_max = "{}".format(self.rule["TOL_MAX"] * self.mm_to_um())
        return "_".join(
            ["{}%".format(self.rule["TOL_PERC"]),
             "max{}".format(self.cut_to_int(tol_max))]
        )

    def mm_to_um(self):
        if self.rule["MM_TO_UM"] == 1:
            return 1000
        else:
            return 1

    def cut_to_int(self, tag):
        if tag[-2:] == ".0":
            return tag[: -2]
        else:
            return tag
