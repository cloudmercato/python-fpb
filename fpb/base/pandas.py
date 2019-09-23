import pandas as pd
from fpb.base import common
from fpb.base import numpy


class BasePandasRunner(numpy.BaseNumpyRunner):
    pd = pd
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'pandas_version': pd.__version__,
    }


class BasePandas1dRunner(common.Runner1dMixin, BasePandasRunner):
    """Helpers for Pandas Runners in 1 dimension array"""
    def prepare(self, size):
        data = self.pd.DataFrame(self.np.random.sample(size))
        return data
