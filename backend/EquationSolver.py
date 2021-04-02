from typing import Optional

import numpy as np
from scipy import linalg

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

    def solve(self, K, C, R, T, Nx):
        if C <= 0 or R <= 0 or K < 0 or T < 0:
            raise ValueError('Некорректное значение коэфициентов. Проверьте правильность ввода')

        def exp_pow(n, t):
            p = -a * a * n * (n + 1) * t / R ** 2
            return np.exp(p) * (2 * n + 1) / 2

        a = K / C

        t = T
        theta = np.linspace(0, np.pi, Nx + 1)
        x = np.cos(theta)
        # term0 = 4
        term0 = 2
        term1 = 20 / 21 * exp_pow(1, t) * x
        term3 = 128 / (21 * 8 * 6) * (5 * x ** 3 - 3 * x) / 2 * exp_pow(3, t)
        term5 = 20480 / (231 * 32 * 120) * (63 * x ** 5 - 70 * x ** 3 + 15 * x) / 8 * exp_pow(5, t)
        return np.round(theta, 3).tolist(), (term0 + term1 + term3 + term5).tolist()


class ImplicitNumericalEquationSolver(metaclass=SingletonEquationSolver):

    def __init__(self):
        self.logger = Logging.get_logger(self.__class__.__name__)
        self.logger.debug('EquationSolver is created')

    def solve(self, K, C, R, T, Nx, Nt):
        if C <= 0 or R <= 0 or K < 0 or Nx <= 0 or Nt <= 0 or T < 0:
            raise ValueError('Некорректное значение коэфициентов. Проверьте правильность ввода')

        xs = np.linspace(0, np.pi, Nx + 1)
        hx = np.pi / Nx
        ht = T / Nt
        u_k = self.__initial_condition(xs)
        a = K / C

        alpha = (a * a * ht) / (hx * hx * R * R)
        beta = (a * a * ht) / (2 * R * R * hx)
        A = np.zeros((Nx + 1, Nx + 1))

        A[0, 0] = 1 + 4 * alpha
        A[0, 1] = -4 * alpha
        for i in range(1, Nx):
            A[i, i - 1] = beta * np.cos(xs[i]) / np.sin(xs[i]) - alpha
            A[i, i] = 1 + 2 * alpha
            A[i, i + 1] = - beta * np.cos(xs[i]) / np.sin(xs[i]) - alpha
        A[Nx, Nx - 1] = -4 * alpha
        A[Nx, Nx] = 1 + 4 * alpha

        for k in range(Nt):
            u_k = linalg.solve(A, u_k)
        return u_k.tolist()

    def __initial_condition(self, xs):
        return 2 + np.power(np.cos(xs), 5) + np.cos(xs)


class ExplicitNumericalEquationSolver(metaclass=SingletonEquationSolver):

    def __init__(self):
        self.logger = Logging.get_logger(self.__class__.__name__)
        self.logger.debug('EquationSolver is created')

    def solve(self, K, C, R, T, Nx, Nt):
        if C <= 0 or R <= 0 or K < 0 or Nx <= 0 or Nt <= 0 or T < 0:
            raise ValueError('Некорректное значение коэфициентов. Проверьте правильность ввода')

        xs = np.linspace(0, np.pi, Nx + 1)
        hx = np.pi / Nx
        ht = T / Nt
        u_k = self.__initial_condition(xs)
        a = K / C

        alpha = (a * a * ht) / (hx * hx * R * R)
        beta = (a * a * ht) / (2 * R * R * hx)
        A = np.zeros((Nx + 1, Nx + 1))

        A[0, 0] = 1 + 4 * alpha
        A[0, 1] = -4 * alpha
        for i in range(1, Nx):
            A[i, i - 1] = beta * np.cos(xs[i]) / np.sin(xs[i]) - alpha
            A[i, i] = 1 + 2 * alpha
            A[i, i + 1] = - beta * np.cos(xs[i]) / np.sin(xs[i]) - alpha
        A[Nx, Nx - 1] = -4 * alpha
        A[Nx, Nx] = 1 + 4 * alpha

        for k in range(Nt):
            u_k = linalg.solve(A, u_k)
        return u_k.tolist()

    def __initial_condition(self, xs):
        return 2 + np.power(np.cos(xs), 5) + np.cos(xs)


if __name__ == '__main__':
    print("Testing solver")
    K = 0.01
    C = 10.24
    R = 5
    Nx = 100
    Nt = 100
    T = 5
    u = ImplicitNumericalEquationSolver().solve(K, C, R, T, Nx, Nt)
    import matplotlib.pyplot as plt

    plt.plot(np.arange(len(u)), u)
    plt.show()
