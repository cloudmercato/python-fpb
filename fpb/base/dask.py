import multiprocessing
import dask
import dask.array as da
import dask.dataframe as dd
from fpb.base import common
from fpb.base import numpy


class BaseDaskRunner(numpy.BaseNumpyRunner):
    dd = dd
    da = da
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'dask_version': dask.__version__,
    }

    scheduler = 'threads'

    def check_output(self, output):
        if self.da.isinf(output).any():
            raise self.TypeTooSmall()


class BaseDask1dRunner(common.Runner1dMixin, BaseDaskRunner):
    """Helpers for Dask Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        chunksize = int(size / multiprocessing.cpu_count())
        data = self.da.random.random(size, chunks=chunksize)\
            .astype(dtype)
        return data


class BaseDask2dRunner(common.Runner2dMixin, BaseDaskRunner):
    """Helpers for Dask Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        chunksize = (int(size / multiprocessing.cpu_count()), 1)
        data = self.da.random\
            .random((size, size_y))\
            .rechunk(chunksize)\
            .astype(dtype)
        return data


class BaseDaskDataframe2dRunner(BaseDask2dRunner):
    """Helpers for Dask Runners in 2 dataframes"""
    def check_output(self, output):
        pass

    def prepare(self, size, size_y, dtype):
        chunksize = (int(size / multiprocessing.cpu_count()), 1)
        da_data = self.da.random\
            .random((size, size_y))\
            .rechunk(chunksize)\
            .astype(dtype)
        data = da_data.to_dask_dataframe()
        return data
