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
    def prepare(self, size, dtype):
        np_data = self.np.random.sample(size).astype(dtype)
        data = self.pd.DataFrame(np_data)
        return data


class BasePandas2dRunner(common.Runner2dMixin, BasePandasRunner):
    """Helpers for Pandas Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        np_data = self.np.random.sample(size*size_y)\
            .reshape(size, size_y)\
            .astype(dtype)
        data = self.pd.DataFrame(np_data, dtype=np_data.dtype)
        return data
