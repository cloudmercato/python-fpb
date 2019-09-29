from fpb.base import dask


class Runner(dask.BaseDask1dRunner):
    def run(self, data):
        output = self.da.sin(data).compute()
        return output
