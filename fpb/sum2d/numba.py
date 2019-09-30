from fpb.base import numba


@numba.nb.njit
def run_(data):
    output = numba.np.sum(data, axis=0)
    return output


class Runner(numba.BaseNumba2dRunner):
    def run(self, data):
        return run_(data)
