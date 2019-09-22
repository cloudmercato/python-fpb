from fpb.base import dask


class Runner(dask.BaseDask1dRunner):
    def run(self, data):
        max_ = self.dd.Aggregation(
            'sum_',
            lambda s: s.max(),
            lambda s0: s0.max()
        )
        output = max_.agg(data).compute()
        return output
