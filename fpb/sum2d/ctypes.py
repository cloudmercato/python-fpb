from fpb.base import ctypes


class Runner(ctypes.BaseCtypes2dRunner):
    def run(self, data):
        output = [
            sum(d) for d in data
        ]
        return output
