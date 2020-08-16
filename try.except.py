try:
    nom = int(input("Give the nominator: "))
    denom = int(input("Give the denominator: "))
    res = nom/denom
except ZeroDivisionError:
    print("Error: Division by zero")