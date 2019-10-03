from fpb.base import dask


class Runner(dask.BaseDaskDataframe2dRunner):
    def run(self, data):
        output = data.corr().compute(scheduler=self.scheduler)
        return output

