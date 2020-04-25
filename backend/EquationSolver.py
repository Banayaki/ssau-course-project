from typing import Optional

import numpy as np

from backend.utils.Logging import Logging


class SingletonEquationSolver(type):
    _instance: Optional = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class EquationSolver(metaclass=SingletonEquationSolver):

    def __init__(self):
        self.logger = Logging.get_logger(self.__class__.__name__)
        self.logger.debug('EquationSolver is created')

    def solve(self, K, C, R, T, lb, rb, max_error):
        xs = np.linspace(lb, rb, 1000)
        x, y = xs, K + xs * C + R * xs ** 2 + T * xs ** 3
        return np.round(x, 4).tolist(), np.round(y, 4).tolist()
