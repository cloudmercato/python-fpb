from fpb.base import numpy


class Runner(numpy.BaseNumpy2dRunner):
    def run(self, data):
        output = self.np.sum(data, axis=1)
        return output
