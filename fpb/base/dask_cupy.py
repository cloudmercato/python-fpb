import cupy as cp
from fpb.base import common
from fpb.base import numpy
from fpb.base import dask


class BaseDaskCupyRunner(dask.BaseDaskRunner):
    cp = cp
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'dask_version': dask.dask.__version__,
        'cupy_version': cp.__version__,
    }
    random = dask.da.random.RandomState(RandomState=cp.random.RandomState)
    scheduler = 'threads'

    def check_output(self, output):
        if self.da.isinf(output).any():
            raise self.TypeTooSmall()


    @property
    def device(self):
        if not hasattr(self, '_device'):
            self._device = cp.cuda.Device(0)
        return self._device

    @property
    def device_processor_count(self):
        if not hasattr(self, '_device_processor_count'):
            self._device_processor_count = self.device.attributes['MultiProcessorCount']
        return self._device_processor_count


class BaseDaskCupy1dRunner(common.Runner1dMixin, BaseDaskCupyRunner):
    """Helpers for Dask CuPy Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        chunksize = size / self.device_processor_count
        data = self.random.random_sample(size, chunks=chunksize)\
            .astype(dtype)
        return data


class BaseDaskCupy2dRunner(common.Runner2dMixin, BaseDaskCupyRunner):
    """Helpers for Dask CuPy Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        chunksize = (1, size)
        data = self.random\
            .random_sample((size_y, size))\
            .rechunk(chunksize)\
            .astype(dtype)
        return data
