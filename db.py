from sqlalchemy import create_engine
import pymysql
import pandas as pd


class DB():

    def __init__(self, ctx):
        self.ctx = ctx
        self.engine = create_engine(
            'mysql+pymysql://root:@localhost:3306/coil_{}?charset=utf8mb4'
            .format(ctx.cfg.get_line())
        )

    def add_quote(self, id):
        return "'" + id + "'"

    def read_cid_table(self, coil_ids):
        query = (" SELECT * FROM cid WHERE coil_id IN({})").format(",".join(
            [self.add_quote(x) for x in coil_ids]))

        df = pd.read_sql(query, self.engine)

        if df.shape[0] == 0:
            raise Exception("the data cannot find in DB")

        df["start_date"] = pd.to_datetime(df["start_date"])

        self.set_cur_dir(df)

        return df

    def set_cur_dir(self, df):

        for idx in df.index:
            coil_id = df.loc[idx, "coil_id"]
            ts = df.loc[idx, "start_date"]
            product_month = self.to_month(ts)
            product_date = self.to_date(ts)
            df.loc[idx, "cur_dir"] = "/".join(
                [self.ctx.root_dir,
                 "{}".format(product_month),
                 "{}".format(product_date),
                 coil_id]
            )

    def to_month(self, ts):
        return ts.year * 100 + ts.month

    def to_date(self, ts):
        return ts.year * 10000 + ts.month * 100 + ts.day

    def merge_cid(self, df):
        # try:
        cid = self.read_cid_table(df["coil_id"])
        df = pd.merge(cid, df, how="left", on="coil_id")
        df.index = df["coil_id"]
        return df
        # except Exception as e:
        #     return df
