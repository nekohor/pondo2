import configparser
from dateutil import parser
from datetime import datetime, timedelta


class Config(object):

    def __init__(self):
        self.dict = {}
        self.conf = configparser.ConfigParser()
        self.conf.read("config_work.ini", encoding="utf-8-sig")
        self.dump_setting()

    def dump_setting(self):
        self.dict["batch_mode"] = self.conf.getboolean("mode", "batch_mode")

        self.dict["line"] = self.conf.get("path", "line")

        self.dict["tables_dir"] = self.conf.get("path", "tables_dir")
        self.dict["root_dir"] = self.get_root_dir()
        self.dict["result_dir"] = self.conf.get("path", "result_dir")

        self.dict["date_array"] = self.get_date_array()

        self.dict["max_array"] = self.conf.getint("data", "max_array")

        self.dict["task_name"] = self.conf.get("task", "task_name")

    def get_root_dir(self):
        if self.dict["line"] == "1580":
            return self.conf.get("path", "root_dir1")
        elif self.dict["line"] == "2250":
            return self.conf.get("path", "root_dir2")
        else:
            raise Exception("wrong mill line")

    def get_date_array(self):
        start_date = self.conf.get("date", "start_date")
        end_date = self.conf.get("date", "end_date")

        start_datetime = parser.parse(start_date)
        end_datetime = parser.parse(end_date)

        days = (end_datetime - start_datetime).days

        date_array = []
        for i in range(days + 1):
            current_datetime = start_datetime + timedelta(days=i)
            date_array.append(current_datetime.strftime("%Y%m%d"))
        print(date_array)
        return date_array

    def get_config_dict(self):
        return self.dict


if __name__ == '__main__':
    config = Config()
    print(config.dict)
