from fpb.base import pycuda


class Runner(pycuda.BasePycuda1dRunner):
    def run(self, data):
        output = self.ga.max(data)
        return output
