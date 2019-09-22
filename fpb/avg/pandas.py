from fpb.base import pandas


class Runner(pandas.BasePandas1dRunner):
    def run(self, data):
        output = data.aggregate(self.np.average)
        return output
