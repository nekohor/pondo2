from context import Context
from cid_table import CoilIdTable
from statistician import Statistician
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
        ctx.cid = CoilIdTable(ctx.db, cur_dir)
        Statistician().stat(ctx, cur_dir, df)

    result_file_path = ctx.get_daily_result_path()
    df.to_excel(result_file_path)


if __name__ == '__main__':
    # data_dir = "d:/predict_train_pool"
    daily_stat()
