N = int(input("Give N: "))
while N<3 or N>20:
    N = int(input("Give N(3-20): "))

numbers = []
for cnt in range(0,N):
    numbers.append(int(input("Give " + str(cnt+1) + "th number: ")))

numbers.sort()

print(numbers)
