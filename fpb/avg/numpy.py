from fpb.base import numpy


class Runner(numpy.BaseNumpy1dRunner):
    def run(self, data):
        output = self.np.average(data)
        return output
