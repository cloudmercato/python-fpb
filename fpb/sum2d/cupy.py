from fpb.base import cupy


class Runner(cupy.BaseCupy2dRunner):
    def run(self, data):
        output = self.cp.sum(data, axis=1)
        output = self.cp.asnumpy(output)
        return output
