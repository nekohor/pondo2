import configparser
from dateutil import parser
from datetime import datetime, timedelta


class Config(object):

    def __init__(self, ctx):
        self.ctx = ctx
        self.dict = {}
        self.conf = configparser.ConfigParser()
        self.conf.read("config.ini", encoding="utf-8-sig")
        self.dump_setting()

    def dump_setting(self):
        self.dict["max_array"] = self.conf.getint("data", "max_array")

        self.dict["batch_mode"] = self.conf.getboolean("mode", "batch_mode")

        self.dict["line"] = self.conf.get("path", "line")

        self.dict["root_dir"] = self.get_root_dir()

        self.dict["export_dir"] = self.conf.get("path", "export_dir")
        self.dict["result_dir"] = self.conf.get("path", "result_dir")

        self.dict["date_array"] = self.get_dates()

        self.dict["task_name"] = self.conf.get("task", "task_name")

        self.dict["factor_mode"] = self.conf.get("factor", "mode")

    def get_line(self):
        return self.dict["line"]

    def get_root_dir(self):
        if self.dict["line"] == "1580":
            return self.conf.get("path", "root_dir1")
        elif self.dict["line"] == "2250":
            return self.conf.get("path", "root_dir2")
        else:
            raise Exception("wrong mill line")

    def get_dates(self):
        start_date = self.conf.get("date", "start_date")
        end_date = self.conf.get("date", "end_date")

        start_datetime = parser.parse(start_date)
        end_datetime = parser.parse(end_date)

        days = (end_datetime - start_datetime).days

        dates = []
        for i in range(days + 1):
            current_datetime = start_datetime + timedelta(days=i)
            dates.append(current_datetime.strftime("%Y%m%d"))
        return dates

    def get_max_array_num(self):
        return self.dict["max_array"]

    def get_task_name(self):
        return self.dict["task_name"]

    def get_factor_mode(self):
        return self.dict["factor_mode"]

    def get_stat_result_dir(self):
        return self.dict["result_dir"]

    def get_crit_result_dir(self):
        return "e:/crit_result_data"

    def get_export_result_dir(self):
        return "e:/export_result_data"

    def get_dict(self):
        return self.dict


if __name__ == '__main__':
    config = Config()
    print(config.dict)
