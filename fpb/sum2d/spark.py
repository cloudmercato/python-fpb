from fpb.base import spark


class Runner(spark.BaseSpark2dRunner):
    def run(self, data):
        output = data.select(*[
            self.functions.sum(c)
            for c in self.col_names
        ]).collect()
        return output
