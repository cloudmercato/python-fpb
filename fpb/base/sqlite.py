import sqlite3
from fpb.base import common

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS fpb (
    id INTEGER PRIMARY KEY,
    x REAL
);
"""
INSERT_1D = "INSERT INTO fpb(x) VALUES(?);"
CREATE_TABLE_2D = """
CREATE TABLE IF NOT EXISTS fpb (
    id INTEGER PRIMARY KEY,
    x REAL,
    y REAL
);
"""
INSERT_2D = "INSERT INTO fpb(x, y) VALUES(?, ?);"
SUM = "SELECT SUM(x) FROM fpb;"
SUM_2D = "SELECT SUM(x), SUM(y)  FROM fpb;"
DROP_TABLE = "DROP TABLE fpb;"


class BaseSqliteRunner(common.Runner):
    extra_data = {
        'sqlite_version': sqlite3.version,
    }

    def get_dtype(self):
        """Used by some framework"""
        return self.dtype

    def check_output(self, output):
        pass

    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = sqlite3.connect(':memory:')
        return self._db

    @property
    def cursor(self):
        if not hasattr(self, '_cursor'):
            self._cursor = self.db.cursor()
        return self._cursor

    def tear_down(self):
        self.cursor.execute(DROP_TABLE)

    def _set_pragma(self):
        self.cursor.execute("PRAGMA shrink_memory")
        self.cursor.execute("PRAGMA journal_mode = OFF")
        # self.cursor.execute("PRAGMA synchronous = 0")


class BaseSqlite1dRunner(common.Runner1dMixin, BaseSqliteRunner):
    """Helpers for SQLite3 Runners in 1 dimension array"""
    def prepare(self, size, **kwargs):
        self._set_pragma()
        data = ((self.random.random(), ) for i in range(size))
        self.cursor.execute(CREATE_TABLE)
        self.cursor.executemany(INSERT_1D, data)
        return data


class BaseSqlite2dRunner(common.Runner2dMixin, BaseSqliteRunner):
    """Helpers for SQLite3 Runners in 2 dimension array"""
    def prepare(self, size, size_y, **kwargs):
        self._set_pragma()
        data = (
            (self.random.random(), self.random.random())
            for i in range(size)
        )
        self.cursor.execute(CREATE_TABLE_2D)
        self.cursor.executemany(INSERT_2D, data)
        return data
