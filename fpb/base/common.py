import sys
import time
import math
import random
import logging

logger = logging.getLogger('fpb.runner')


class TypeTooSmall(Exception):
    pass


class Runner:
    """Base class for all runner."""
    random = random
    math = math
    extra_data = {}
    _dtype = None

    TypeTooSmall = TypeTooSmall

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            logger.debug("Set '%s' = '%s'", key, value)
            setattr(self, key, value)

    def get_dtype(self):
        """Used by some framework"""
        return self._dtype

    def get_prepare_kwargs(self):
        return {}

    def get_run_kwargs(self):
        return {}

    def check_output(self, output):
        pass

    def start(self):
        logger.info("Prepare test")
        prepare_kwargs = self.get_prepare_kwargs()
        logger.debug("Prepare kwargs: %s", prepare_kwargs)
        prepare_kwargs['dtype'] = self.get_dtype()
        data = self.prepare(**prepare_kwargs)
        input_size = sys.getsizeof(data)
        logger.debug("Prepare done")

        logger.info("Run test")
        run_kwargs = self.get_run_kwargs()
        logger.debug("Run kwargs: %s", run_kwargs)
        start_time = time.time()
        output = self.run(data, **run_kwargs)
        end_time = time.time()
        logger.debug("Run done")

        self.check_output(output)
        return (
            (end_time - start_time) * 1000,
            input_size,
        )

    def prepare(self, **kwargs):
        msg = "Data preparation isn't set."
        raise NotImplementedError(msg)

    def run(self, data, **kwargs):
        msg = "Run isn't set."
        raise NotImplementedError(msg)


class Runner1dMixin:
    def get_prepare_kwargs(self):
        return {
            'size': self.size,
        }


class Runner2dMixin:
    def get_prepare_kwargs(self):
        return {
            'size': self.size,
            'size_y': self.size_y,
        }
