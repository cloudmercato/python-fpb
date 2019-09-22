import time
import math
import random


class Runner:
    """Base class for all runner."""
    random = random
    math = math

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_prepare_kwargs(self):
        return {}

    def get_run_kwargs(self):
        return {}

    def start(self):
        prepare_kwargs = self.get_prepare_kwargs()
        data = self.prepare(**prepare_kwargs)

        run_kwargs = self.get_run_kwargs()
        start_time = time.time()
        output = self.run(data, **run_kwargs)
        end_time = time.time()
        return end_time - start_time

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
