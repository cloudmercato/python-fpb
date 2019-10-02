from fpb.base import dask_cupy


class Runner(dask_cupy.BaseDaskCupy2dRunner):
    def run(self, data):
        output = self.da.sum(data, axis=1).compute(scheduler=self.scheduler)
        return output
