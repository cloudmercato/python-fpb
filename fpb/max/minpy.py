from fpb.base import minpy


class Runner(minpy.BaseMinpy1dRunner):
    context_unit = 'gpu'
    policy = 'only_mxnet'

    def run(self, data):
        output = self.np.max(data)
        return output
