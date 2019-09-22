from fpb.base import python


class Runner(python.BasePython1dRunner):
    def run(self, data):
        output = max(data)
        return output
