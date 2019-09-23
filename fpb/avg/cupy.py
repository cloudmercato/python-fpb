from fpb.base import cupy


class Runner(cupy.BaseCupy1dRunner):
    def run(self, data):
        output = self.cp.average(data)
        return output
