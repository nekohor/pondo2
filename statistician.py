import pandas as pd

from context import Context

from client import SocketClient
from records import Records
from coils import Coils
from calculator import Calculator
from criteria import Criteria
import logging


class Statistician():
    def __init__(self):
        self.ctx = Context()

    def socket_stat(self, df, ids=None, cur_dir=None):

        if cur_dir:

            coil_ids = self.ctx.direct.get_coil_ids(cur_dir)
            logging.info(coil_ids)
        elif ids:
            coil_ids = ids

        self.ctx.records = Records(self.ctx, coil_ids, cur_dir)
        self.ctx.cli = SocketClient(self.ctx)

        for coil_id in self.ctx.records.get_coil_ids():
            df.loc[coil_id, "coil_id"] = coil_id

            self.ctx.coils = Coils(self.ctx, coil_id)

            for task_idx in self.ctx.task.get_idxs():

                rule = self.ctx.task.get_rule(task_idx)
                result = Calculator(self.ctx, coil_id, rule).calc()

                col_name = self.ctx.task.get_col_name(task_idx)
                df.loc[coil_id, col_name] = result
                print(cur_dir, coil_id, col_name, result)

    def batch_stat(self):
        df = pd.DataFrame()
        for date_dir in self.ctx.direct.get_date_dirs():
            self.socket_stat(df, cur_dir=date_dir)
        df = self.ctx.db.merge_cid(df)

        self.ctx.direct.save_batch_stat(df)

        # if self.ctx.task.is_access_db():
        #     Criteria(self.ctx, df).run()

    def specific_stat(self, coil_ids):
        df = pd.DataFrame()
        for date_dir in self.ctx.direct.get_date_dirs():
            self.socket_stat(df, ids=coil_ids)
        self.ctx.direct.save_specific_stat(df)
