from fpb.base import numexpr


class Runner(numexpr.BaseNumexpr1dRunner):
    def run(self, data):
        count = data.shape[0]
        sum_ = self.ne.evaluate('sum(data)')
        output = self.ne.evaluate('sum_ / count')
        return output
