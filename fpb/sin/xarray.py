from fpb.base import xarray


class Runner(xarray.BaseXarray1dRunner):
    def run(self, data):
        output = self.xr.apply_ufunc(self.np.sin, data)
        return output
