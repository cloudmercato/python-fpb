from fpb.base import python


class Runner(python.BasePythonGen2dRunner):
    def run(self, data):
        output = [sum(d) for d in data]
        return output
