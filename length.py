

class Length():

    def __init__(self, ctx, rule, id_record):
        self.line = ctx.line
        self.rule = rule

        coil_id = id_record["coil_id"]
        self.build_hdtl(ctx.cid.table.loc[coil_id, "coil_len"])
        self.build_cut()

    def build_cut(self):
        self.head_cut = 5
        self.tail_cut = 5

    def build_hdtl(self, coil_len):
        if self.rule["LENGTH_MODE"] == "bite":
            self.build_bite()
        elif self.rule["LENGTH_MODE"] == "feedback":
            self.build_feedback()
        elif self.rule["LENGTH_MODE"] == "average":
            self.build_average(coil_len)
        elif self.rule["LENGTH_MODE"] == "r2dt":
            self.build_r2dt()

    def build_bite(self):
        if "1580" == self.line:
            self.head_len = 120
            self.tail_len = 50
        elif "2250" == self.line:
            self.head_len = 150
            self.tail_len = 50
        else:
            raise Exception("wrong line")

    def build_feedback(self):
        self.head_len = 50
        self.tail_len = 50

    def build_average(self, coil_len):
        self.head_len = coil_len * 0.333
        self.tail_len = coil_len * 0.333

    def build_r2dt(self):
        self.head_len = 166
        self.tail_len = 166

    def get_head_len(self):
        return self.head_len

    def get_tail_len(self):
        return self.tail_len

    def get_head_cut(self):
        return self.head_cut

    def get_tail_cut(self):
        return self.tail_cut
