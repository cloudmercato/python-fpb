from fpb.base import mpmath


class Runner(mpmath.BaseMpmath2dRunner):
    def run(self, data):
        fsum = self.mm.fsum
        output = [fsum(d) for d in data]
        return output
