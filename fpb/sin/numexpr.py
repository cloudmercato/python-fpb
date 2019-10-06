from fpb.base import numexpr


class Runner(numexpr.BaseNumexpr1dRunner):
    def run(self, data):
        output = self.ne.evaluate('sin(data)')
        return output
