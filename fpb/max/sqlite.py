from fpb.base import sqlite


class Runner(sqlite.BaseSqlite1dRunner):
    def run(self, data):
        output = tuple(self.cursor.execute(sqlite.MAX))[0][0]
        return output
