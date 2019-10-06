import xarray as xr
from fpb.base import common
from fpb.base import numpy


class BaseXarrayRunner(numpy.BaseNumpyRunner):
    xr = xr
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'xarray_version': xr.__version__,
    }


class BaseXarray1dRunner(common.Runner1dMixin, BaseXarrayRunner):
    """Helpers for Xarray Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        np_data = self.np.random.sample(size).astype(dtype)
        data = xr.DataArray(np_data)
        return data


class BaseXarray2dRunner(common.Runner2dMixin, BaseXarrayRunner):
    """Helpers for Xarray Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        np_data = self.np.random.sample(size*size_y)\
            .reshape(size, size_y)\
            .astype(dtype)
        data = xr.DataArray(np_data, dims=('x', 'y'))
        return data
