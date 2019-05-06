import pandas as pd

import sys
import os

from config import Config
from parts import Parts
from task import Task
from db import DB
from directory import Directory
# from records import Records

import json
import logging


class Context:

    def __init__(self):

        self.cfg = Config(self)
        self.line = self.cfg.get_line()
        self.root_dir = self.cfg.get_root_dir()

        self.partbl = Parts(self)
        self.task = Task(self)

        self.db = DB(self)
        self.direct = Directory(self)

    def get_cur_dir_by_now(self):
        return sys.argv[2].replace("\\", "/")

    def get_batch_result_path(self):
        result_path = self.cfg.get_result_dir()
        result_path += "/{}_{}_{}_{}.xlsx".format(
            self.line,
            self.cfg.get_task_name(),
            self.cfg.get_dates()[0],
            self.cfg.get_dates()[-1]
        )
        return result_path

    # about exported data
    def get_exported_data_dir(self, date):
        return "{}/{}/{}".format(
            self.cfg["export_dir"], date[:6])

    def get_exported_data_json_path(self, date):
        return "{}/{}/{}/{}".format(
            self.ctx.cfg["export_dir"],
            self.ctx.line,
            date[:6],
            "ExportedData_{}_{}.json".format(
                self.ctx.line,
                date
            )
        )

    def get_exported_data_json(self, date):
        logging.info(self.get_exported_data_json_path(date))
        coils = {}
        with open(self.get_exported_data_json_path(date), "r") as json_file:
            coils = json.load(json_file)
        return coils
