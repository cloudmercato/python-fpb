from fpb.base import ctypes


class Runner(ctypes.BaseCtypes1dRunner):
    def run(self, data):
        output = data[0]
        size = len(data)
        for i in range(1, size):
            output = i if i > data[i] else output
        return output
