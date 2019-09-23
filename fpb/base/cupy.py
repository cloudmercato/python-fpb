import cupy as cp
from fpb.base import common


class BaseCupyRunner(common.Runner):
    cp = cp
    extra_data = {
        'cupy_version': cp.__version__
    }


class BaseCupy1dRunner(common.Runner1dMixin, BaseCupyRunner):
    """Helpers for Cupy Runners in 1 dimension array"""
    def prepare(self, size):
        data = self.cp.random.sample(size)
        return data
