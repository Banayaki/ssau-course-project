from typing import Optional

import numpy as np
from utils.Logging import Logging


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

    def solve(self, K, C, R, T):
        if C <= 0 or R <= 0 or K < 0 or T < 0:
            raise ValueError('Некорректное значение коэфициентов. Проверьте правильность ввода')

        def exp_pow(n, t):
            p = -a * a * n * (n + 1) * t / R ** 2
            return np.exp(p) * (2 * n + 1) / 2

        a = K / C

        t = T
        theta = np.linspace(0, np.pi, 1000)
        x = np.cos(theta)
        term0 = 4
        term1 = 20 / 21 * exp_pow(1, t) * x
        term3 = 128 / (21 * 8 * 6) * (5 * x ** 3 - 3 * x) / 2 * exp_pow(3, t)
        term5 = 20480 / (231 * 32 * 120) * (63 * x ** 5 - 70 * x ** 3 + 15 * x) / 8 * exp_pow(5, t)
        return np.round(theta, 3).tolist(), (term0 + term1 + term3 + term5).tolist()
