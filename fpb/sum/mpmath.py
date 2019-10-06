from fpb.base import mpmath


class Runner(mpmath.BaseMpmath1dRunner):
    def run(self, data):
        fsum = self.mm.fsum
        output = fsum(data)
        return output
