from fpb.base import numpy


class Runner(numpy.BaseNumpy1dRunner):
    def run(self, data):
        output = self.np.sum(data)
        return output
