from fpb.base import mpmath_gmpy


class Runner(mpmath_gmpy.BaseMpmathGmpy21dRunner):
    def run(self, data):
        fsum = self.mm.fsum
        output = fsum(data)
        return output
