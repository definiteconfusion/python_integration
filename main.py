import numpy as np
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
    

c = Calc(12, 0, 0.01, "2**(-1*(x-5))")
print(c.Integrate())