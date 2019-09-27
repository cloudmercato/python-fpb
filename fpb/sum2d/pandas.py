from fpb.base import pandas


class Runner(pandas.BasePandas2dRunner):
    def run(self, data):
        output = data.sum()
        return output
