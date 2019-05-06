import pandas as pd


class Records:
    def __init__(self, ctx, coil_ids, cur_dir=None):
        self.ctx = ctx
        self.coil_ids = coil_ids
        self.cur_dir = cur_dir

        self.table = self.set_table()

    def set_table(self):

        if self.ctx.task.is_access_db():
            df = self.ctx.db.read_cid_table(self.coil_ids)
        else:
            df = pd.DataFrame()
            df["coil_id"] = self.coil_ids

        if self.cur_dir:
            df["cur_dir"] = self.cur_dir

        df.index = df["coil_id"]

        df = self.select_hot_run(df)

        return df

    def get_record(self, coil_id):
        return self.table.loc[coil_id]

    def get_cur_dir(self, coil_id):
        return self.table.loc[coil_id]["cur_dir"]

    def get_coil_ids(self):
        return self.table["coil_id"]

    def select_hot_run(self, df):
        startswith_M = df["coil_id"].apply(
            lambda x: str(x).startswith("M")
        )
        startswith_H = df["coil_id"].apply(
            lambda x: str(x).startswith("H")
        )
        # print(startswith_M)
        # print(startswith_H)
        return df.loc[startswith_M | startswith_H]
