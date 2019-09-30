from fpb.base import ctypes


class Runner(ctypes.BaseCtypes1dRunner):
    def run(self, data):
        output = sum(data) / len(data)
        return output
