import ctypes
from fpb.base import common


class Runner(common.Runner):
    dtypes = {
        'float32': 'c_float',
        'float64': 'c_double',
        'float128': 'c_longdouble',
    }

    def get_dtype(self):
        if self.dtype not in self.dtypes:
            msg = "Invalid type '%s'" % self.dtype
            raise TypeError(msg)
        return self.dtypes[self.dtype]


class BaseCtypes1dRunner(common.Runner1dMixin, Runner):
    """Helpers for ctypes Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        ctype = getattr(ctypes, dtype)
        data = (ctype * size)(*[self.random.random() for i in range(size)])
        return data


class BaseCtypes2dRunner(common.Runner2dMixin, Runner):
    """Helpers for ctypes Runners in 2 dimension array"""
    def prepare(self, size, size_y):
        data = [
            [self.random.random() for j in range(size_y)]
            for i in range(size)
        ]
        return data
