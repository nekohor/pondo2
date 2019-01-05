import numpy as np


class Tolerance():

    def __init__(self, rule, id_record):
        self.rule = rule
        self.id_record = id_record
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
        if str(self.rule["AIM"])[0] == "0":
            return 0
        else:
            return self.id_record["aim_{}".format(self.rule["AIM"])]

    def get_tol(self):
        if self.rule["TOL"] == 0:
            return self.get_tol_by_thk()
        else:
            return self.rule["TOL"]

    def get_tol_by_thk(self):
        tol = (self.rule["TOL_PERC"] / 100 *
               self.id_record["aim_thick"])
        return np.minimum(tol, self.rule["TOL_MAX"])

    def get_upper(self):
        return self.upper

    def get_lower(self):
        return self.lower
