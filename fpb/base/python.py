from fpb.base import common


class BasePython1dRunner(common.Runner1dMixin, common.Runner):
    """Helpers for Runners in 1 dimension array"""
    def prepare(self, size):
        data = [self.random.random() for i in range(size)]
        return data
