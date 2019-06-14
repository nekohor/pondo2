import pandas as pd


class Parts:

    def __init__(self, ctx):
        self.line = ctx.cfg.get_line()
        self.table = pd.read_excel("tables/partTable.xlsx")
        self.table = self.table.loc[self.table["LINE"] == int(self.line)]
        self.table.index = self.table["PART"]

    def get_signal_name(self, part):
        # return self.table.loc[part, "SIGNAL"]
        return self.table.loc[part, "SIGNAL"].replace('\\\\', '\\')

    def get_dca_file_name(self, part):
        return self.table.loc[part, "DCAFILE"] + ".dca"
