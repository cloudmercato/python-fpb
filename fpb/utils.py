"""Utils module."""
import importlib

DTYPES = (
    'float16',
    'float32',
    'float64',
    'float128',
)
OPERATIONS = (
    'sum',
    'sum2d',
    'sin',
    'avg',
    'max',
)
MODULES = (
    'python',
    'python_gen',
    'ctypes',
    'numpy',
    'pandas',
    'dask',
    'cupy',
    'minpy',
    'numba',
)
RUNNERS = []


def import_runner(operation, module):
    module_path = 'fpb.%s.%s' % (operation, module)
    runner_mod = importlib.import_module(module_path)
    return runner_mod


for operation in OPERATIONS:
    for module_name in MODULES:
        try:
            runner_mod = import_runner(operation, module_name)
        except ImportError as err:
            if err.name.startswith('fpb.'):
                continue
        runner_path = '%s.%s' % (operation, module_name)
        RUNNERS.append(runner_path)
