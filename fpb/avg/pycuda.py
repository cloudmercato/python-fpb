from fpb.base import pycuda


class Runner(pycuda.BasePycuda1dRunner):
    def run(self, data):
        output = self.ga.sum(data) / data.shape[0]
        return output
