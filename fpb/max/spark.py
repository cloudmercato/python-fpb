from fpb.base import spark


class Runner(spark.BaseSpark1dRunner):
    def run(self, data):
        output = data.select(self.functions.max('x')).collect()[0][0]
        return output
