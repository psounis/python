def max3(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


x = input("Give a number: ")
y = input("Give a number: ")
z = input("Give a number: ")

n = max3(x, y, z)

for i in range(n):
    sq = i*i
    print(sq)