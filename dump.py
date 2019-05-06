# from exe import Exe
# from length import Length
# from factor import Factor
# from tolerance import Tolerance

# from cid_table import CoilIdTable
# from data_json import DataJson


def pondex_stat(self, ctx, date, df):
    cur_dir, is_exist = ctx.get_cur_dir_by_date(date)
    coil_id_list = ctx.get_coil_id_list(cur_dir)
    ctx.cid = CoilIdTable(ctx.db, coil_id_list)
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
            executor.set_length(Length(ctx, rule, id_record))
            executor.set_upper_lower(Tolerance(rule, id_record))

            col_name = ctx.tasks.col_list[task_id]
            exec_result = executor.execute()
            df.loc[coil_id, col_name] = exec_result

            logging.info(dca_path, col_name, exec_result)
        # i += 1
        # if i > 0:
        #     break


def secondary_stat(self, ctx, date, df):
    coils = ctx.get_exported_data_json(date)
    djson = DataJson(ctx, coils)
    coil_id_list = djson.get_coil_id_list()
    ctx.cid = CoilIdTable(ctx.db, coil_id_list)

    for coil_id in ctx.cid.table.index:
        id_record = ctx.cid.table.loc[coil_id]
        for task_id in ctx.tasks.table.index:
            rule = ctx.tasks.table.loc[task_id]

            calc_result = djson.calc(rule, id_record)
            col_name = ctx.tasks.col_list[task_id]

            df.loc[coil_id, col_name] = calc_result
            logging.info(id_record["start_date"],
                         coil_id, col_name, calc_result)
