from bound import Run
eq = "2**(-1*(x-5))"
acc = 0.1
start = 0.0
print(Run('./python_bound', eq, acc, start))