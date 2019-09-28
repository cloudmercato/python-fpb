from fpb.base import common


class BasePython1dRunner(common.Runner1dMixin, common.Runner):
    """Helpers for Runners in 1 dimension array"""
    def prepare(self, size, **kwargs):
        data = [self.random.random() for i in range(size)]
        return data


class BasePython2dRunner(common.Runner2dMixin, common.Runner):
    """Helpers for Runners in 2 dimension array"""
    def prepare(self, size, size_y, **kwargs):
        data = [
            [self.random.random() for j in range(size_y)]
            for i in range(size)
        ]
        return data


class BasePythonGen1dRunner(common.Runner1dMixin, common.Runner):
    """Helpers for Runners in 1 dimension array with generator"""
    def prepare(self, size, **kwargs):
        data = (self.random.random() for i in range(size))
        return data


class BasePythonGen2dRunner(common.Runner2dMixin, common.Runner):
    """Helpers for Runners in 2 dimension array with generator"""
    def prepare(self, size, size_y, **kwargs):
        data = (
            (self.random.random() for j in range(size_y))
            for i in range(size)
        )
        return data
