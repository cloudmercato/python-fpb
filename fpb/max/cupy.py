from fpb.base import cupy


class Runner(cupy.BaseCupy1dRunner):
    def run(self, data):
        output = data.max()
        return output
