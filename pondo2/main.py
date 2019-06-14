import pandas as pd
from statistician import Statistician
from context import Context
from criteria import Criteria
from exporter import Exporter

import rollen

import logging
logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)

if __name__ == '__main__':

    ctx = Context()

    Statistician(ctx).batch_stat()

    # df = pd.read_excel("d:/work/专题/硅钢同板差/all_tag2.xlsx")
    # Statistician(ctx).specific_stat(df["coil_id"])

    # df = pd.read_excel(ctx.direct.get_batch_stat_result_path())
    # Criteria(ctx, df).evaluate()

    # line = 1580
    # start_mdate = 201901
    # end_mdate = 201905
    # table_name = "cid"

    # rln = rollen.roll(line)
    # mdates = rln.time.get_month_dates(start_mdate, end_mdate)

    # df = rln.db.table(table_name).where("month", "in", mdates).get()
    # df = rln.grade.select(df, "steel_grade", ["MGW350D", "MGW350"])

    # Exporter(ctx).specific_export(df["coil_id"])
