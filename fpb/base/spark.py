import pyspark
from pyspark.sql import types
from pyspark.sql import functions

from fpb.base import common
from fpb.base import numpy


class BaseSparkRunner(numpy.BaseNumpyRunner):
    functions = functions
    extra_data = {
        'numpy_version': numpy.np.__version__,
        'pyspark_version': pyspark.__version__,
    }

    @property
    def spark_context(self):
        if not hasattr(self, '_sql'):
            self._spark_context = pyspark.SparkContext(
                appName='fpb',
            )
        return self._spark_context

    @property
    def sql(self):
        if not hasattr(self, '_sql'):
            self._sql = pyspark.SQLContext(self.spark_context)
        return self._sql


class BaseSpark1dRunner(numpy.BaseNumpy1dRunner, BaseSparkRunner):
    """Helpers for Spark Runners in 1 dimension array"""
    def prepare(self, size, dtype):
        np_data = super().prepare(size=size, dtype=dtype)
        np_data = np_data.reshape(size, 1)
        data = self.sql.createDataFrame(np_data.tolist(), ['x'])
        return data


class BaseSpark2dRunner(numpy.BaseNumpy2dRunner, BaseSparkRunner):
    """Helpers for Spark Runners in 2 dimension array"""
    def prepare(self, size, size_y, dtype):
        np_data = super().prepare(size=size, size_y=size_y, dtype=dtype)
        self.col_names = [str(i) for i in range(size_y)]
        data = self.sql.createDataFrame(np_data.tolist(), self.col_names)
        return data

