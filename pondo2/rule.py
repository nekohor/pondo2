
class Rule():

    def __init__(self, ctx, task_idx):
        self.ctx = ctx
        self.rule = self.ctx.task.table.loc[task_idx]

    def get_len_mode(self):
        return self.rule["LENGTH_MODE"]

    def get_factor(self):
        return self.rule["FACTOR"]

    def get_segment(self):
        return self.rule["SEGMENT"]

    def get_func_tag(self):
        return self.rule["STAT_FN"]

    def get_tol(self):
        return self.rule["TOL"]
