from fpb.base import python


class Runner(python.BasePython1dRunner):
    def run(self, data):
        output = sum(data) / len(data)
        return output
