x = [[1,2], [3,4]]
y = x.copy()
print(f"x:{x} x:{id(x)}, x[0]:{id(x[0])}, x[1]:{id(x[1])}")
print(f"y:{y} y:{id(y)}, y[0]:{id(y[0])}, y[1]:{id(y[1])}")
x[0].append(0)
print(f"x:{x} y:{y}")