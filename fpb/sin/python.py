from fpb.base import python


class Runner(python.BasePython1dRunner):
    def run(self, data):
        output = [self.math.sin(x) for x in data]
        return output
