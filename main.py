import pandas as pd
from statistician import Statistician
import logging
logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)

if __name__ == '__main__':
    Statistician().batch_stat()
