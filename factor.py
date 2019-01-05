class Factor():

    def __init__(self, factor_name):
        self.factor_name = factor_name
        self.parts = self.build_parts()

    def build_parts(self):
        part_list = []
        if self.factor_name[:8] == "leveling":
            std = self.factor_name[-1]
            part_list.extend(
                ["os_gap{}".format(std), "ds_gap{}".format(std)])
        elif self.factor_name == "asym_flt":
            part_list.extend(["flt_ro1", "flt_ro5"])
        elif self.factor_name == "sym_flt":
            part_list.extend(["flt_ro3", "flt_ro1", "flt_ro5"])
        else:
            part_list.extend([self.factor_name])
        return part_list

    def get_parts(self):
        return self.parts

    def get_signals(self, ctx):
        return [ctx.partbl.get_signal_name(p) for p in self.parts]
