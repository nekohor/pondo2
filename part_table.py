import pandas as pd


class PartTable:

    def __init__(self, line, tables_dir):
        self.table = pd.read_excel(tables_dir + "/tables/part_table.xlsx")
        self.table = self.table.loc[self.table["LINE"] == int(line)]
        self.table.index = self.table["PART"]

    def get_signal_name(self, part):
        # return self.table.loc[part, "SIGNAL"]
        return self.table.loc[part, "SIGNAL"].replace('\\\\', '\\')

    def get_dca_file_name(self, part):
        return self.table.loc[part, "DCAFILE"] + ".dca"
