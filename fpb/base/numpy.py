import numpy as np
from fpb.base import common


class BaseNumpyRunner(common.Runner):
    np = np
    extra_data = {
        'numpy_version': np.__version__
    }

    def get_dtype(self):
        """Used by some framework"""
        return self.dtype

    def check_output(self, output):
        if self.np.isinf(output).all().any():
            raise self.TypeTooSmall()



class BaseNumpy1dRunner(common.Runner1dMixin, BaseNumpyRunner):
    """Helpers for Numpy Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        data = self.np.random.sample(size).astype(dtype)
        return data


class BaseNumpy2dRunner(common.Runner2dMixin, BaseNumpyRunner):
    """Helpers for Numpy Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        data = self.np.random.sample(size*size_y)\
            .reshape(size, size_y)\
            .astype(dtype)
        return data
