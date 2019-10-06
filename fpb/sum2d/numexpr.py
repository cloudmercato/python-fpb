from fpb.base import numexpr


class Runner(numexpr.BaseNumexpr2dRunner):
    def run(self, data):
        output = self.ne.evaluate('sum(data, axis=0)')
        return output
