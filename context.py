import pandas as pd
from config import Config
import sys

from part_table import PartTable
from task_table import TaskTable
from cid_table import CoilIdTable
from db import DB


class Context:

    def __init__(self):

        self.cfg = Config().get_config_dict()
        self.line = self.cfg["line"]
        self.partbl = PartTable(self.line, self.cfg["tables_dir"])
        self.tasks = TaskTable(self.line, self.cfg["task_name"])
        self.db = DB(self.line)
        self.cid = "CoilIdTable()"

    def get_cur_dir_by_date(self, date):
        return "{}/{}/{}".format(
            self.cfg["root_dir"],
            date[:6],
            date
        )

    def get_cur_dir_by_now(self):
        return sys.argv[2].replace("\\", "/")

    def get_dca_path(self, cur_dir, coil_id, signals):
        part = signals[0]
        return "{}/{}/{}".format(
            cur_dir, coil_id, self.partbl.get_dca_file_name(part))

    def get_daily_result_path(self):
        result_path = self.cfg["result_dir"] + "/"
        result_path += "{}_{}_{}_{}.xlsx".format(
            self.line,
            self.cfg["task_name"],
            self.cfg["date_array"][0],
            self.cfg["date_array"][-1]
        )
        return result_path
