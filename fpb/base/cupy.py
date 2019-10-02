import cupy as cp
from fpb.base import common


class BaseCupyRunner(common.Runner):
    cp = cp
    extra_data = {
        'cupy_version': cp.__version__
    }

    def get_dtype(self):
        """Used by some framework"""
        return self.dtype


class BaseCupy1dRunner(common.Runner1dMixin, BaseCupyRunner):
    """Helpers for Cupy Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        data = self.cp.random.sample(size).astype(dtype)
        return data


class BaseCupy2dRunner(common.Runner2dMixin, BaseCupyRunner):
    """Helpers for Cupy Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        data = self.cp.random.sample(size*size_y)\
            .reshape(size_y, size)\
            .astype(dtype)
        return data
