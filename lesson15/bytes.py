x = 15
b = x.to_bytes(4, byteorder='big')
print(b)
n = int.from_bytes(b, byteorder='big')
print(n)
