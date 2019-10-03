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

    memory_error_codes = [
        'CURAND_STATUS_ALLOCATION_FAILED',
        'CURAND_STATUS_PREEXISTING_FAILURE',
    ]

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
        chunksize = int(size / self.device_processor_count)
        chunksize = max([chunksize, 10e9])
        try:
            data = self.random.random_sample(size, chunks=chunksize)\
                .astype(dtype)
        except self.cp.cuda.curand.CURANDError as err:
            if err.args[0] in self.memory_error_codes:
                raise MemoryError(err.args[0])
            raise
        return data


class BaseDaskCupy2dRunner(common.Runner2dMixin, BaseDaskCupyRunner):
    """Helpers for Dask CuPy Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        chunksize = (1, size)
        try:
            data = self.random\
                .random_sample((size_y, size))\
                .rechunk(chunksize)\
                .astype(dtype)
        except self.cp.cuda.curand.CURANDError as err:
            if err.args[0] in self.memory_error_codes:
                raise MemoryError(err.args[0])
            raise
        return data
