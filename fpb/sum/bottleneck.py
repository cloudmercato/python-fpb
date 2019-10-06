from fpb.base import bottleneck


class Runner(bottleneck.BaseBottleneck1dRunner):
    def run(self, data):
        output = self.bn.nansum(data)
        return output
