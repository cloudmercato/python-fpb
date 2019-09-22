from fpb.base import dask


class Runner(dask.BaseDask1dRunner):
    def run(self, data):
        output = data.apply(self.np.sin, meta=(None, 'float64'))
        return output
