from fpb.base import xarray


class Runner(xarray.BaseXarray1dRunner):
    def run(self, data):
        output = data.mean()
        return output
