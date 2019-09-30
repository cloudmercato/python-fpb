import numba as nb
import numpy as np
from fpb.base import common
from fpb.base import numpy


class BaseNumbaRunner(numpy.BaseNumpyRunner):
    nb = nb
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'numba_version': nb.__version__,
    }


class BaseNumba1dRunner(common.Runner1dMixin, BaseNumbaRunner):
    """Helpers for Numba Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        data = self.np.random.sample(size).astype(dtype)
        return data


class BaseNumba2dRunner(common.Runner2dMixin, BaseNumbaRunner):
    """Helpers for Numba Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        data = self.np.random.sample(size*size_y)\
            .reshape(size, size_y)\
            .astype(dtype)
        return data
