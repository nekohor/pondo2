import toml


class Factor():

    def __init__(self, ctx):
        self.ctx = ctx

        self.stds = [1, 2, 3, 4, 5, 6, 7]

        self.mode = self.ctx.cfg.get_factor_mode()

        self.toml_factors = {}

        self.toml_factors["all"] = toml.load("factors/factors_all.toml")
        self.toml_factors["specific"] = toml.load(
            "factors/factors_specific.toml")

    def get_factors(self):
        factors = getattr(self, "get_{}_factors".format(self.mode))()
        return factors

    def get_all_factors(self):
        factors = []
        for group_factors in self.toml_factors["all"]["factors"]:
            if group_factors["group"] == "fm_stand":

                for std in self.stds:
                    factors.extend(
                        [x + str(std) for x in group_factors["factorNames"]]
                    )

            else:
                factors.extend(group_factors["factorNames"])

        return factors

    def get_specific_factors(self):
        factors = []
        for group_factors in self.toml_factors["specific"]["factors"]:
            factors.extend(group_factors["factorNames"])
        return factors

    def get_task_factors(self):
        return self.ctx.task.get_factors()
