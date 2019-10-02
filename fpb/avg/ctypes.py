from fpb.base import ctypes


class Runner(ctypes.BaseCtypes1dRunner):
    def run(self, data):
        output = 0
        size = len(data)
        for i in range(size):
            output += output + data[i]
        output = output / size
        return output
