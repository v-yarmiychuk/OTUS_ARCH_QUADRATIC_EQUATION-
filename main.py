from math import isclose
from math import sqrt
from typing import List, Union

import matplotlib.pyplot as plt
import numpy as np


class QuadraticEquation:
    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> None:
        self._a = a
        self._b = b
        self._c = c

        self._delta = None
        self._x_0 = None
        self._x_1 = None
        self._x_2 = None

    def solve(self) -> List[float]:
        a, b, c = float(self._a), float(self._b), float(self._c)

        if isclose(a, 0, abs_tol=1e-05):
            raise ValueError('Not a Quadratic Equation')

        self._delta = delta = b ** 2 - 4 * a * c

        if isclose(delta, 0, abs_tol=1e-05):
            self._x_0 = -b / (2 * a)
            ret = [self._x_0, ]
        elif delta < 0:
            ret = []
        else:
            self._x_1 = (-b - sqrt(delta)) / (2 * a)
            self._x_2 = (-b + sqrt(delta)) / (2 * a)
            ret = [self._x_1, self._x_2]

        return ret

    def draw(self) -> None:
        self.solve()
        a, b, c = float(self._a), float(self._b), float(self._c)

        plt.axhline(y=0)
        plt.axvline(x=0)
        plt.title(
            f'y= {a}x²'
            f'{"+" if b >= 0 else "-"}{str(abs(b))}x'
            f'{"+" if c >= 0 else "-"}{str(abs(c))}'
        )

        if isclose(self._delta, 0, abs_tol=1e-05):
            plt.plot(self._x_0, 0, marker="o", color='k')
        elif self._delta > 0:
            plt.plot(self._x_1, 0, marker="o", color='k')
            plt.plot(self._x_2, 0, marker="o", color='k')

        if self._x_0:
            x = np.linspace(self._x_0 - 5, self._x_0 + 5, 100)
        elif self._x_1 and self._x_2:
            x = np.linspace(self._x_1 - 1, self._x_2 + 1, 100)
        else:
            x = np.linspace(-5, 5, 100)

        y = a * x ** 2 + b * x + c

        plt.plot(x, y, color='k')

        plt.show()


if __name__ == '__main__':
    QuadraticEquation(1, 0, 1).draw()
    QuadraticEquation(1, 0, -1).draw()
    QuadraticEquation(1, 2, 1).draw()
    QuadraticEquation(1, 0, 0.0000000001).draw()
