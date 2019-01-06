from context import Context
from cid_table import CoilIdTable
from statistician import Statistician
from data_json import DataJson
import pandas as pd


def current_stat(data_dir):
    ctx = Context()


def daily_stat():
    ctx = Context()
    df = pd.DataFrame()
    for date in ctx.cfg["date_array"]:
        print(date)
        cur_dir = ctx.get_cur_dir_by_date(date)
        print(cur_dir)
        coil_id_list = ctx.get_coil_id_list(cur_dir)
        ctx.cid = CoilIdTable(ctx.db, coil_id_list)
        Statistician().stat(ctx, cur_dir, df)

    result_file_path = ctx.get_daily_result_path()
    df.to_excel(result_file_path)


def secondary_stat():
    ctx = Context()
    df = pd.DataFrame()
    for date in ctx.cfg["date_array"]:
        print(date)
        djson = DataJson(ctx, date)
        coil_id_list = djson.get_coil_id_list()
        ctx.cid = CoilIdTable(ctx.db, coil_id_list)
        Statistician().secondary_stat(ctx, djson, df)

    result_file_path = ctx.get_daily_result_path()
    df.to_excel(result_file_path)


if __name__ == '__main__':
    # data_dir = "d:/predict_train_pool"
    # daily_stat()
    secondary_stat()
