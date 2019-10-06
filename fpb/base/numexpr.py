import numexpr as ne
from fpb.base import common
from fpb.base import numpy


class BaseNumexprRunner(numpy.BaseNumpyRunner):
    ne = ne
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'numeprx_version': ne.__version__,
    }


class BaseNumexpr1dRunner(common.Runner1dMixin, BaseNumexprRunner):
    """Helpers for NumExpr Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        data = self.np.random.sample(size).astype(dtype)
        return data


class BaseNumexpr2dRunner(common.Runner2dMixin, BaseNumexprRunner):
    """Helpers for NumExpr Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        data = self.np.random.sample(size*size_y)\
            .reshape(size, size_y)\
            .astype(dtype)
        return data

