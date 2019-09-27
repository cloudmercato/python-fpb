from fpb.base import numpy


class Runner(numpy.BaseNumpy2dRunner):
    def run(self, data):
        output = self.np.sum(data, axis=0, dtype="float128")
        return output
