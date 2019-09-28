from fpb.base import ctypes


class Runner(ctypes.BaseCtypes1dRunner):
    def run(self, data):
        output = 0
        for i in range(len(data)):
            output += output + data[i]
        return output
