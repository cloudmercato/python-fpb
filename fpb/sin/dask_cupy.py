from fpb.base import dask_cupy


class Runner(dask_cupy.BaseDaskCupy1dRunner):
    def run(self, data):
        output = self.da.sin(data).compute(scheduler=self.scheduler)
        return output
