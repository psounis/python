number = int(input("Enter a number(0-9): "))
while number < 0 or number > 9:
    number = int(input("Between 0 and 9 please: "))

print("You entered: " + str(number))