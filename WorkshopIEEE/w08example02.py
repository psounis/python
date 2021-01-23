def square_cube(number):
    return number ** 2, number ** 3


num = 5
square, cube = square_cube(num)
print(f"{num}^2={square}, {num}^3={cube}")