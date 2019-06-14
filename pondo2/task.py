import pandas as pd
from column import Column
from rule import Rule


class Task:

    def __init__(self, ctx):
        self.ctx = ctx
        self.task_path = "tasks/task_table_{}.xlsx".format(
            ctx.cfg.get_task_name())
        self.table = pd.read_excel(self.task_path)

        self.col_list = self.create_col_list()

        self.table["col_name"] = self.col_list
        self.table.to_excel("tmp/tmp_task.xlsx")

    def create_col_list(self):
        col_list = []
        for idx in self.table.index:
            rule = self.table.loc[idx]
            col_list.append(Column(rule).get_col())
        return col_list

    def get_col_list(self):
        # a list for schemas
        if hasattr(self, "col_list"):
            return self.col_list
        else:
            raise("please call create_col_list() at __init__")

    def get_factors(self):
        return list(self.table["FACTOR"].drop_duplicates())

    def get_idxs(self):
        return self.table.index

    def get_rule(self, idx):
        return Rule(self.ctx, idx)

    def get_col_name(self, idx):
        return self.col_list[idx]

    def is_access_db(self):

        for aim in self.table["AIM"]:

            if str(aim) == "nan":
                continue
            elif str(aim)[0] == "0":
                continue
            else:
                return True

        return False
