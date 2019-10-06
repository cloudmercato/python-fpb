from fpb.base import bottleneck


class Runner(bottleneck.BaseBottleneck2dRunner):
    def run(self, data):
        output = self.np.nansum(data, axis=0)
        return output
