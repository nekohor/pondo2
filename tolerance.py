import numpy as np


class Tolerance():

    def __init__(self, ctx, coil_id, rule):
        self.ctx = ctx
        self.coil_id = coil_id
        self.rule = rule.rule
        self.record = self.ctx.records.get_record(coil_id)
        self.build_tolerance()

    def build_tolerance(self):
        if np.isnan(self.rule["UPPER"]) & np.isnan(self.rule["LOWER"]):
            self.build_limit()
        else:
            self.upper = self.rule["UPPER"]
            self.lower = self.rule["LOWER"]

    def build_limit(self):
        aim = self.get_aim()
        tol = self.get_tol()
        self.lower = aim - tol
        self.upper = aim + tol

    def get_aim(self):

        if self.rule["STAT_FN"] != "aimrate":
            return 0

        if str(self.rule["AIM"])[0] == "0":
            return 0
        else:
            return self.record["aim_{}".format(self.rule["AIM"])]

    def get_tol(self):
        if self.rule["TOL"] == 0:
            return self.get_tol_by_thk()
        else:
            return self.rule["TOL"]

    def get_tol_by_thk(self):
        tol = (self.rule["TOL_PERC"] / 100 *
               self.record["aim_thick"])
        return np.minimum(tol, self.rule["TOL_MAX"])

    def get_upper(self):
        return self.upper

    def get_lower(self):
        return self.lower
