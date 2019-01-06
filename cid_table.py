
import pandas as pd


class CoilIdTable:
    def __init__(self, db, coil_id_list):
        self.db = db
        self.coil_id_list = [self.add_quote(x) for x in coil_id_list]
        self.table = self.read_cid_table()

    def add_quote(self, id):
        return "'" + id + "'"

    def read_cid_table(self):
        query = (" SELECT * FROM cid WHERE coil_id IN({})").format(",".join(
            self.coil_id_list))

        df = pd.read_sql(query, self.db.engine)
        if df.shape[0] == 0:
            raise Exception("the data cannot find in DB")
        df.index = df["coil_id"]
        return df
