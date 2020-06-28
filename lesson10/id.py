x = 5
print(f"x: {id(x)}, 5: {id(5)}")
y = 5
print(f"y: {id(y)}")
x = 6
print(f"x: {id(x)}, 6: {id(6)}")
y = x
print(f"x: {id(x)}, y: {id(y)}")