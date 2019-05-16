import pandas as pd
from statistician import Statistician
from context import Context
from criteria import Criteria


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

    # df = pd.read_excel(ctx.direct.get_batch_stat_result_path())
    # Criteria(ctx, df).evaluate()
