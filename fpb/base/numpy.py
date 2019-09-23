import numpy as np
from fpb.base import common


class BaseNumpyRunner(common.Runner):
    np = np
    extra_data = {
        'numpy_version': np.__version__
    }


class BaseNumpy1dRunner(common.Runner1dMixin, BaseNumpyRunner):
    """Helpers for Numpy Runners in 1 dimension array"""
    def prepare(self, size):
        data = self.np.random.sample(size)
        return data
