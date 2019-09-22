from fpb.base import pandas


class Runner(pandas.BasePandas1dRunner):
    def run(self, data):
        output = data.apply(self.np.sin)
        return output
