import os
import pandas as pd


class Directory:

    def __init__(self, ctx):
        self.ctx = ctx

    def get_date_dir(self, date):
        date_dir = "{}/{}/{}".format(
            self.ctx.cfg.get_root_dir(),
            date[:6],
            date
        )
        return date_dir

    def get_date_dirs(self):

        date_dirs = []
        for date in self.ctx.cfg.get_dates():
            cur_dir = self.get_date_dir(date)

            if os.path.exists(cur_dir):
                date_dirs.append(cur_dir)
            else:
                continue
        return date_dirs

    def get_coil_ids(self, cur_dir):
        coil_ids = os.listdir(cur_dir)
        return [x for x in coil_ids if os.path.isdir(cur_dir + "/" + x)]

    def get_coil_id_dirs(self, cur_dir):
        coil_ids = self.get_coil_ids(cur_dir)
        return [(cur_dir + "/" + x) for x in coil_ids]

    def get_batch_stat_result_path(self):
        result_path = self.ctx.cfg.get_result_dir()
        result_path += "/{}_{}_{}_{}.xlsx".format(
            self.ctx.line,
            self.ctx.cfg.get_task_name(),
            self.ctx.cfg.get_dates()[0],
            self.ctx.cfg.get_dates()[-1]
        )
        return result_path

    def save_batch_stat(self, df):

        save_path = self.get_batch_stat_result_path()
        df.to_excel(save_path)
