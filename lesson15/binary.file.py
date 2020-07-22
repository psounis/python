numbers = [1,2,3,4]
with open("binary.dat", "wb") as f:
    for number in numbers:
        f.write(number.to_bytes(4, byteorder='big'))

with open("binary.dat", "rb") as f:
    for i in range(len(numbers)):
        b = f.read(4)
        print(int.from_bytes(b, byteorder='big'))
