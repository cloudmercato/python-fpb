from fpb.base import spark


class Runner(spark.BaseSpark1dRunner):
    def run(self, data):
        output = data.select(self.functions.sin('x')).collect()
        return output

