from fpb.base import xarray


class Runner(xarray.BaseXarray2dRunner):
    def run(self, data):
        output = data.sum(axis=0, dtype="float128")
        return output
