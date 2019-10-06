import bottleneck as bn
from fpb.base import common
from fpb.base import numpy


class BaseBottleneckRunner(numpy.BaseNumpyRunner):
    bn = bn
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'bottleneck_version': bn.__version__,
    }


class BaseBottleneck1dRunner(common.Runner1dMixin, BaseBottleneckRunner):
    """Helpers for Bottleneck Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        data = self.np.random.sample(size).astype(dtype)
        return data


class BaseBottleneck2dRunner(common.Runner2dMixin, BaseBottleneckRunner):
    """Helpers for Bottleneck Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        data = self.np.random.sample(size*size_y)\
            .reshape(size, size_y)\
            .astype(dtype)
        return data
