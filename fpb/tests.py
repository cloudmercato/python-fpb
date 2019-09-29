import sys
import unittest
import importlib

OPERATIONS = [
    'sum',
    'sum2d',
    'sin',
    'avg',
    'max',
]
MODULES = [
    'python',
    'python_gen',
    'ctypes',
    'numpy',
    'pandas',
    'dask',
    'cupy',
    'minpy',
    'numba',
    'sqlite',
]

def import_runner(operation, module):
    module_path = 'fpb.%s.%s' % (operation, module)
    runner_mod = importlib.import_module(module_path)
    return runner_mod


def make_test_case(operation, module, skip=False):
    class RunnerTest(unittest.TestCase):
        runner_args = {
            'size': 100,
            'size_y': 3,
            'dtype': 'float32',
        }

        def __repr__(self):
            return '%s%sTestCase' % (self.operation.capitalize(),
                                     self.module.capitalize())

        def __str__(self):
            return "%s (%s)" % (self._testMethodName, self.__repr__())

        def setUp(self):
            self._skip_due_to_requirement()
            runner_mod = import_runner(self.operation, self.module)
            self.runner = runner_mod.Runner(**self.runner_args)

        def _skip_due_to_requirement(self):
            if self.skip_all:
                msg = "%s not available" % self.module
                self.skipTest(msg)

        def test_start(self):
            output = self.runner.start()


    RunnerTest.operation = operation
    RunnerTest.module = module
    RunnerTest.skip_all = skip
    test_name = '%s%sTestCase' % (operation.capitalize(), module.capitalize())
    RunnerTest.__name__ = test_name
    return RunnerTest


def get_suite():
    suite = unittest.TestSuite()
    for operation in OPERATIONS:
        for module_name in MODULES:
            try:
                runner_mod = import_runner(operation, module_name)
                skip = False
            except ImportError as err:
                if err.name.startswith('fpb.'):
                    continue
                skip = True
            case = make_test_case(operation, module_name, skip)
            tests = unittest.defaultTestLoader.loadTestsFromTestCase(case)
            suite.addTest(tests)
    return suite


if __name__ == '__main__':
    suite = get_suite()
    test_runner = unittest.TextTestRunner(verbosity=5)
    test_runner.run(suite)
