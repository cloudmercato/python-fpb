from fpb.base import dask


class Runner(dask.BaseDask1dRunner):
    def run(self, data):
        output = self.da.average(data).compute(scheduler=self.scheduler)
        return output
