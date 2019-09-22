from fpb.base import dask


class Runner(dask.BaseDask1dRunner):
    def run(self, data):
        sum_ = self.dd.Aggregation(
            'sum_',
            lambda s: s.sum(),
            lambda s0: s0.sum()
        )
        output = sum_.agg(data).compute()
        return output
