import gmpy2
import os
import importlib
import mpmath as mm

os.environ.pop('MPMATH_NOGMPY', None)
importlib.reload(mm)


from fpb.base import common
from fpb.base import mpmath


class BaseMpmathGmpy2Runner(mpmath.BaseMpmathRunner):
    pass


class BaseMpmathGmpy21dRunner(mpmath.BaseMpmath1dRunner):
    """Helpers for Mpmath gmpy2 Runners in 1 dimension array"""


class BaseMpmathGmpy22dRunner(mpmath.BaseMpmath2dRunner):
    """Helpers for Mpmath gmpy2 Runners in 2 dimension array"""
