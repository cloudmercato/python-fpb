import pycuda as pc
import pycuda.gpuarray as ga
import pycuda.curandom as random

from fpb.base import common
from fpb.base import numpy


class BasePycudaRunner(numpy.BaseNumpyRunner):
    pc = pc
    ga = ga
    random = random
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'pycuda_version': pc.VERSION_TEXT,
    }

    def check_output(self, output):
        pass

    def prepare(self, **kwargss):
        import pycuda.autoinit


class BasePycuda1dRunner(common.Runner1dMixin, BasePycudaRunner):
    """Helpers for PyCUDA Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        super().prepare(size=size, dtype=dtype)
        dtype = getattr(self.np, dtype)
        data = self.random.rand(size, dtype=dtype)
        return data


class BasePycuda2dRunner(common.Runner2dMixin, BasePycudaRunner):
    """Helpers for PyCUDA Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        super().prepare(size=size, size_y=size_y, dtype=dtype)
        dtype = getattr(self.np, dtype)
        data = self.random.rand(size*size_y, dtype=dtype)\
            .reshape(size, size_y)
        return data
