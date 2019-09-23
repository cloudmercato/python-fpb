from fpb.base import numba


@numba.nb.njit
def run_(data):
    sum_ = numba.np.sum(data)
    output = sum_ / data.size
    return data


class Runner(numba.BaseNumba1dRunner):
    def run(self, data):
        return run_(data)
