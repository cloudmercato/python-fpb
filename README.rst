Python Floating Point Benchmark
===============================

**FPB** is a simple tool to measure differentt ways to make computation in Python.
The goal is to understand what are the best ways to apply or aggregate data accross many ways.

Features
--------

Operations
~~~~~~~~~~

- **Sum** : Sum of a list/array
- **Average** : Average of list/array
- **Max** : Max of list/array
- **Sinus** : Apply sinus function to a list/array
- **Sum 2D** : Sum each list/array
- **Correlation** : Statistical correlation (not yet)

Tools and libraries
~~~~~~~~~~~~~~~~~~~

- **Python** : Standard libraries such as math or builtins
- `NumPy <https://numpy.org/>`_ : Fundamental package for scientific computing with Python
- `Pandas <https://pandas.pydata.org/>`_ : high-performance, easy-to-use data structures and data analysis tools
- `Dask <https://dask.org/>`_ : Advanced parallelism for analytics, enabling performance at scale
- `CuPy <https://cupy.chainer.org/>`_ : NumPy-compatible matrix library accelerated by CUDA
- `Numba <https://numba.pydata.org/>`_ : Translates a subset of Python and NumPy code into fast machine code
- `MinPy <https://github.com/dmlc/minpy>`_ : NumPy interface above MXNet backend (deprecated)
- `SQLite <https://sqlite.org/index.html>`_ : C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. (for fun)

Install
-------

::

  pip install fpb
  
  
Usage
-----

The command is pretty simple to use: ::

  usage: fpb [-h] [-i ITERATIONS] [-v] [-j] [-s SIZE] [-S SIZE_Y] [-d DTYPE]
             [-W WARMUP]
             {sum.python,sum.ctypes,sum.numpy,sum.pandas,sum.dask,sum.cupy,sum.minpy,sum.numba,sum2d.python,sum2d.python_gen,sum2d.numpy,sum2d.pandas,sum2d.dask,sin.python,sin.numpy,sin.pandas,sin.dask,sin.cupy,sin.minpy,sin.numba,avg.python,avg.numpy,avg.pandas,avg.cupy,avg.minpy,avg.numba,max.python,max.numpy,max.pandas,max.dask,max.cupy,max.minpy,max.numba}

  Measure Python computation performances

  positional arguments:
    {sum.python,sum.ctypes,sum.numpy,sum.pandas,sum.dask,sum.cupy,sum.minpy,sum.numba,sum2d.python,sum2d.python_gen,sum2d.numpy,sum2d.pandas,sum2d.dask,sin.python,sin.numpy,sin.pandas,sin.dask,sin.cupy,sin.minpy,sin.numba,avg.python,avg.numpy,avg.pandas,avg.cupy,avg.minpy,avg.numba,max.python,max.numpy,max.pandas,max.dask,max.cupy,max.minpy,max.numba}
                          Module to test.

  optional arguments:
    -h, --help            show this help message and exit
    -i ITERATIONS, --iterations ITERATIONS
                          Number of iteration to run.
    -v, --verbose         Verbosity level.
    -j, --json            Display output as JSON instead of plain text.
    -s SIZE, --size SIZE  Number of element in X axis.
    -S SIZE_Y, --size_y SIZE_Y
                          Number of element in Y axis, for 2D computation.
    -d {float16,float32,float64,float128}, --dtype {float16,float32,float64,float128}
                          Data type storing elements
    -W WARMUP, --warmup WARMUP
                          Number of iteration to run before start test.
                          
Here's an example of output: ::

  $ fpb sin.numpy -i 3 -s 1000000 -d float16
  values         : [14.111995697021484, 14.101982116699219, 14.655590057373047]
  memory_errors  : 0
  size           : 1000000
  test           : fpb.sin.numpy
  iterations     : 3
  python_version : 3.6.8 (default, Aug 20 2019, 17:12:48) [GCC 8.3.0]
  dtype          : float16
  numpy_version  : 1.17.2
  byte_size      : 2000096
  average        : 14.28985595703125
  stddev         : 0.258645371196851
  percentile_99  : 14.644718170166016
  percentile_95  : 14.60123062133789
  percentile_90  : 14.546871185302734
  percentile_75  : 14.383792877197266
  median         : 14.111995697021484
  min            : 14.101982116699219
  max            : 14.655590057373047
  speed          : 71.42422555255513
  


Design consideration
--------------------

- All tests are supposed to be the most efficient way to do in the current framework.
- Data are prepared before the the test and this operation isn't counted in result.
- The task timing represents the time to compute and retrieve the result into Python interpreter, not lazy results.
- Filled memory errors are considered as a normal behavior and counted in result as `memory_errors`.
- When sharding is required to dispatch data, we split it with the number of threads available.
