from fpb.base import ctypes


class Runner(ctypes.BaseCtypes1dRunner):
    def run(self, data):
        output = [
            self.math.sin(d) for d in data
        ]
        return output
