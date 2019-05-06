

class HeadTail():

    def __init__(self, ctx, coil_id, rule):
        self.ctx = ctx
        self.coil_id = coil_id
        self.rule = rule

        self.build_len()
        self.build_cut()

    def build_cut(self):
        self.head_cut = 5
        self.tail_cut = 5

    def build_len(self):
        getattr(
            self, "build_{}".format(self.rule.get_len_mode())
        )()

    def build_bite(self):
        if "1580" == self.ctx.line:
            self.head_len = 120
            self.tail_len = 50
        elif "2250" == self.ctx.line:
            self.head_len = 150
            self.tail_len = 60
        else:
            raise Exception("wrong line")

    def build_feedback(self):
        self.head_len = 50
        self.tail_len = 50

    def build_average(self):
        factor = self.rule.get_factor()
        data_length = len(self.ctx.coils.get_data(self.coil_id, factor))
        self.head_len = data_length * 0.333
        self.tail_len = data_length * 0.333

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
