import pandas as pd
import numpy as np
import rollen

from rollen.query import DataFrameQueryBuilder


class Criteria():

    def __init__(self, ctx, df_stat):
        self.ctx = ctx
        self.df_stat = df_stat
        self.df_stat.index = self.df_stat["coil_id"]

        self.table = pd.read_excel(
            "criterias/criteria_{}.xlsx".format(self.ctx.cfg.get_task_name()))

        self.df_crit = pd.DataFrame(index=self.df_stat.index)

        primary_cols = ["coil_id", "steel_grade",
                        "aim_thick", "aim_width", "start_date"]

        self.df_crit[primary_cols] = self.df_stat[primary_cols]

        self.rln = rollen.tool()

    def select_columns(self):

        print(self.df_stat.shape)
        self.df_stat["aim_wid"] = self.df_stat["aim_width"]
        self.df_stat["aim_thk"] = self.df_stat["aim_thick"]

        for idx in self.table.index:

            cond = self.table.loc[idx]

            # query = self.select_div(cond)

            q = DataFrameQueryBuilder().table(self.df_stat)

            divs = ["wid", "thk"]
            lims = ["min", "max"]

            for div in divs:
                for lim in lims:

                    val = "{}_{}_val".format(div, lim)
                    oper = "{}_{}_oper".format(div, lim)
                    div_col = "aim_{}".format(div)

                    if np.isnan(cond[val]):
                        pass
                    else:
                        print(cond[oper])
                        print(type(cond[oper]))

                        print(cond[val])
                        print(type(cond[val]))

                        q = q.where(
                            div_col, cond[oper], cond[val])

            df = q.get()

            print(df.shape)

            df = self.rln.grade.select(df, "steel_grade", cond["grade_catego"])

            self.df_crit.loc[df.index, "grade_catego"] = (
                cond["grade_catego"]
            )

            self.df_crit[cond["final_col_name"]] = (
                df[cond["selected_col_name"]]
            )

        # self.df_crit.to_excel("df_crit.xlsx")

    def select_div(self, cond):

        q = DataFrameQueryBuilder().table(self.df_stat)

        divs = ["wid", "thk"]
        lims = ["min", "max"]

        for div in divs:
            for lim in lims:
                print("now")

                val = "{}_{}_val".format(div, lim)
                oper = "{}_{}_oper".format(div, lim)
                div_col = "aim_{}".format(div)

                if np.isnan(cond[val]):
                    pass
                else:
                    print(cond[oper])
                    print(cond[val])

                    q = q.where(
                        div_col, cond[oper], cond[div])

        return q

    def rate(self):
