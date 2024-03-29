from fpb.base import numba


@numba.nb.njit
def run_(data):
    output = data.max()
    return output


class Runner(numba.BaseNumba1dRunner):
    def run(self, data):
        return run_(data)
