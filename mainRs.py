# This script is 26x slower than the native Python version

import numpy as np
from bound import *


class Calc:
    def __init__(self, upper_bound, lower_bound, accuracy, equation) -> None:
        self.Z = upper_bound
        self.A = lower_bound
        self.B = accuracy
        self.fX = equation

    @staticmethod
    def Area(eq, acc, start):
        return float(Run('./python_bound', eq, acc, start))

    def Integrate(self):
        return sum([Calc.Area(self.fX, self.B, i) for i in np.arange(self.A, self.Z, self.B)])

c = Calc(12, 0, 0.01, "2^(-1*(x-5))")
print(c.Integrate())