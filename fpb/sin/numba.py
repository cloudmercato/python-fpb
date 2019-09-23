from fpb.base import numba


@numba.nb.njit
def run_(data):
    output = numba.np.sin(data)
    return data


class Runner(numba.BaseNumba1dRunner):
    def run(self, data):
        return run_(data)
