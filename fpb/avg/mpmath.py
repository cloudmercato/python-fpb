from fpb.base import mpmath


class Runner(mpmath.BaseMpmath1dRunner):
    def run(self, data):
        fsum = self.mm.fsum
        fdiv = self.mm.fdiv
        output = fdiv(fsum(data), len(data))
        return output
