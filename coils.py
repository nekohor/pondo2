import numpy as np
import pandas as pd


class Coils():
    """docstring for Luggage"""

    def __init__(self, ctx, coil_ids):
        self.ctx = ctx
        self.coils = self.ctx.cli.get_response(coil_ids)

    def get_coil_ids(self):
        return self.coils.keys()

    def get_data(self, coil_id, factor):
        return pd.Series(self.coils[coil_id]["factors"][factor]["data"])
