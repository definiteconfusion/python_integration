# This script is 26x slower than the native Python version
# Although I'm sure its the `subprocess` lib not Rust
import numpy as np
import matplotlib.pyplot as plt
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
    
    def Graph(self):
        x = np.arange(self.A, self.Z, self.B)
        y = [eval(self.fX.replace('x', str(val))) for val in x]
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label='y = sin(x)', color='blue')


        # Add labels and title
        plt.title('Sine Function with Limits and Shading')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black',linewidth=0.5, ls='--')
        plt.axvline(3, color='red', ls='--', label='x = 3 (Limit Start)')
        plt.axvline(5, color='red', ls='--', label='x = 5 (Limit End)')
        plt.grid()
        plt.legend()

        # Show the plot
        plt.show()


c = Calc(12, 0, 0.01, "2^(-1*(x-5))")
print(c.Integrate())
c.Graph()