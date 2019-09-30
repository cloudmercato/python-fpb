from fpb.base import cupy


class Runner(cupy.BaseCupy1dRunner):
    def run(self, data):
        output = data.max()
        output = self.cp.asnumpy(output)
        return output
