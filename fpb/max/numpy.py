from fpb.base import numpy


class Runner(numpy.BaseNumpy1dRunner):
    def run(self, data):
        output = data.max()
        return output
