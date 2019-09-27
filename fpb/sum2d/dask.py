from fpb.base import dask


class Runner(dask.BaseDask2dRunner):
    def run(self, data):
        output = data.sum(0, dtype='float128').compute()
        return output
