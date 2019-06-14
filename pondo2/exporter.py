import pandas as pd

from client import SocketClient
from records import Records
from coils import Coils

import logging


class Exporter():
    def __init__(self, ctx):
        self.ctx = ctx

    def socket_export(self, ids=None, cur_dir=None):

        if cur_dir:
            coil_ids = self.ctx.direct.get_coil_ids(cur_dir)
            logging.info(coil_ids)
        else:
            coil_ids = ids

        self.ctx.records = Records(self.ctx, coil_ids, cur_dir)
        self.ctx.cli = SocketClient(self.ctx)

        for factor_name in self.ctx.factor.get_factors():

            df = pd.DataFrame(index=range(self.ctx.cfg.get_max_array_num()))

            for coil_id in self.ctx.records.get_coil_ids():

                self.ctx.coils = Coils(self.ctx, coil_id)

                df[coil_id] = self.ctx.coils.get_data(coil_id, factor_name)

                print(
                    self.ctx.records.get_cur_dir(coil_id),
                    coil_id
                )

            if cur_dir:

            else:
                self.ctx.direct.save_specific_export(
                    df, factor_name, coil_ids)

    def batch_export(self):
        pass

    def current_export(self, cur_dir):
        self.socket_export(cur_dir=cur_dir)

    def specific_export(self, coil_ids):
        self.socket_export(ids=coil_ids)
