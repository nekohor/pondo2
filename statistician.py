import pandas as pd
from exe import Exe
from length import Length
from factor import Factor
from tolerance import Tolerance


class Statistician():
    def __init__(self):
        pass

    def stat(self, ctx, cur_dir, df):

        # i = 0
        for coil_id in ctx.cid.table.index:
            id_record = ctx.cid.table.loc[coil_id]
            for task_id in ctx.tasks.table.index:
                rule = ctx.tasks.table.loc[task_id]

                executor = Exe()

                parts = Factor(rule["FACTOR"]).get_parts()
                signals = Factor(rule["FACTOR"]).get_signals(ctx)
                executor.set_signals(signals)

                dca_path = ctx.get_dca_path(cur_dir, coil_id, parts)
                executor.set_dcapath(dca_path)

                executor.set_stat_fn(rule["STAT_FN"])
                executor.set_segment(rule["SEGMENT"])
                executor.set_length(
                    Length(ctx.line, rule,
                           ctx.cid.table.loc[coil_id, "coil_len"]))
                executor.set_upper_lower(Tolerance(rule, id_record))

                col_name = ctx.tasks.col_list[task_id]
                exec_result = executor.execute()
                df.loc[coil_id, col_name] = exec_result

                print(dca_path, col_name, exec_result)
            # i += 1
            # if i > 0:
            #     break
