from fpb.base import cudamat


class Runner(cudamat.BaseCudamat2dRunner):
    def run(self, data):
        output = self.cm.sum(data, axis=0).asarray()
        return output
