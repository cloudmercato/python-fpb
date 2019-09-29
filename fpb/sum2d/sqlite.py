from fpb.base import sqlite


class Runner(sqlite.BaseSqlite2dRunner):
    def run(self, data):
        output = tuple(self.cursor.execute(sqlite.SUM_2D))[0]
        return output
