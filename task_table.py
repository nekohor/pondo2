import pandas as pd
from column import Column


class TaskTable:

    def __init__(self, line, task_name):
        self.line = line
        self.table = pd.read_excel(
            "tasks/task_table_{}.xlsx".format(task_name))

        self.col_list = self.get_col_list()

    def get_col_list(self):
        # a list for schema dict
        col_list = []
        for idx in self.table.index:
            record = self.table.loc[idx]
            col_list.append(Column(record).get_col())
        return col_list
