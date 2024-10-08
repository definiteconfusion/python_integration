import numpy as np
import matplotlib.pyplot as plt
import math
class Calc:
    def __init__(self, upper_bound, lower_bound, accuracy, equation) -> None:
        self.Z = upper_bound
        self.A = lower_bound
        self.B = accuracy
        self.fX = equation
        
    def Area(eq, acc, start):
        eq_start = eq.replace("x", f"({start})")
        fX = eval(eq_start)
        eq_end = eq.replace("x", f"({start + acc})")
        fXB = eval(eq_end)
        return ((fXB * acc) + (acc * (fX - fXB)))
    
    def Integrate(self):
        return sum([Calc.Area(self.fX, self.B, i) for i in np.arange(self.A, self.Z, self.B)])
    
    def Graph(self):
        x = np.arange(self.A, self.Z, self.B)
        y = [eval(self.fX.replace('x', str(val))) for val in x]
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f'y = {self.fX}', color='blue')
        plt.title('Sine Function with Limits and Shading')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black',linewidth=0.5, ls='--')
        plt.axvline(self.A, color='red', ls='--', label=f'x = {self.A} (Limit Start)')
        plt.axvline(self.Z, color='red', ls='--', label=f'x = {self.Z} (Limit End)')
        plt.axvline(self.Z, color='green', ls=' ', label=f'Area = {self.Integrate()}')
        plt.grid()
        plt.legend()
        plt.show()

c = Calc(2*math.pi, 0, 0.0001, "math.sin(x)+1")
c.Graph()