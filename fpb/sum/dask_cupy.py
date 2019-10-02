from fpb.base import dask_cupy


class Runner(dask_cupy.BaseDaskCupy1dRunner):
    def run(self, data):
        output = data.sum().compute(scheduler=self.scheduler)
        return output
