import minpy as mp
from fpb.base import common
from fpb.base import numpy


class BaseMinpyRunner(numpy.BaseNumpyRunner):
    mp = mp
    np = mp.numpy
    extra_data = {
        # 'minpy_version': mp.__version__,
        'mxnet_version': mp.mx.__version__,
    }

    def prepare(self, size):
        self.context = mp.context.Context(self.context_unit, 0)
        mp.context.set_context(self.context)
        mp.set_global_policy(self.policy)        


class BaseMinpy1dRunner(common.Runner1dMixin, BaseMinpyRunner):
    """Helpers for MinPy Runners in 1 dimension array"""
    def prepare(self, size):
        super().prepare(size)
        data = self.np.random.sample(size)
        return data
