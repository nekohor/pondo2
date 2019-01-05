import os
import pandas as pd


class CoilIdTable:
    def __init__(self, db, cur_dir):
        self.db = db
        self.cur_dir = cur_dir

        self.coil_id_list = self.get_coil_id_list()
        self.table = self.read_cid_table()

    def get_coil_id_list(self):
        path_list = os.listdir(self.cur_dir)
        dirs = [x for x in path_list if os.path.isdir(self.cur_dir + "/" + x)]

        coil_id_list = [self.add_quote(x) for x in dirs]

        return coil_id_list

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
