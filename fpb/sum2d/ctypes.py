from fpb.base import ctypes


class Runner(ctypes.BaseCtypes2dRunner):
    def run(self, data):
        output = [.0] * self.size_y
        # data = (ctype * size)(*[self.random.random() for i in range(size)])
        for y in range(self.size_y):
            for x in range(self.size):
                output[y] = output[y] + data[y][x]
        return output
