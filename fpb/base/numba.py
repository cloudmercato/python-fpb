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
    def prepare(self, size):
        data = self.np.random.sample(size)
        return data
