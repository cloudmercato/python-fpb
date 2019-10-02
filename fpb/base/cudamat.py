import cudamat as cm
from fpb.base import common
from fpb.base import numpy


class BaseCudamatRunner(numpy.BaseNumpyRunner):
    cm = cm
    extra_data = {
        'numpy_version': numpy.np.__version__,
    }

    def prepare(self, *args, **kwargs):
        self.cm.cuda_set_device(0)


class BaseCudamat1dRunner(common.Runner1dMixin, BaseCudamatRunner):
    """Helpers for CUDAMAT Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        super().prepare(size, dtype)
        max_ones = size
        self.cm.cublas_init(max_ones)
        self.cm.init(max_ones)

        np_data = self.np.random.sample(size)\
            .reshape(1, size)\
            .astype(dtype)
        data = self.cm.CUDAMatrix(np_data)
        return data


class BaseCudamat2dRunner(common.Runner2dMixin, BaseCudamatRunner):
    """Helpers for CUDAMat Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        super().prepare(size, size_y, dtype)
        max_ones = size * size_y
        self.cm.cublas_init(max_ones)
        self.cm.init(max_ones)

        np_data = self.np.random.sample(size*size_y)\
            .reshape(size, size_y)\
            .astype(dtype)
        data = self.cm.CUDAMatrix(np_data)
        return data
