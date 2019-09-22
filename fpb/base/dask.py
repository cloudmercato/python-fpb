import dask.dataframe as dd
from fpb.base import common
from fpb.base import numpy


class BaseDaskRunner(numpy.BaseNumpyRunner):
    dd = dd


class BaseDask1dRunner(common.Runner1dMixin, BaseDaskRunner):
    """Helpers for Dask Runners in 1 dimension array"""
    def prepare(self, size):
        data = self.dd.from_array(self.np.random.sample(size))
        return data
