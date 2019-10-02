from fpb.base import cudamat


class Runner(cudamat.BaseCudamat1dRunner):
    def run(self, data):
        output = self.cm.sum(data, axis=1).asarray() / data.shape[1]
        return output[0][0]
