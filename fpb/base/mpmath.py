import mpmath as mm
from fpb.base import common


class BaseMpmathRunner(common.Runner):
    mm = mm
    extra_data = {
        'mpmath': mm.__version__
    }


class BaseMpmath1dRunner(common.Runner1dMixin, BaseMpmathRunner):
    """Helpers for Mpmath Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        data = [self.mm.rand() for i in range(size)]
        return data


class BaseMpmath2dRunner(common.Runner2dMixin, BaseMpmathRunner):
    """Helpers for Mpmath Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        data = [
            [self.mm.rand() for j in range(size)]
            for i in range(size_y)
        ]
        return data
