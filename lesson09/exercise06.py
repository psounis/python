while True:
    string = input("Give name: ")
    string = string.strip()

    if string.isalpha():
        name = string.capitalize()
        print(f"Name entered: {name}")
        break
    else:
        print("only characters please! ")

while True:
    string = input("Give surname: ")
    string = string.strip()

    if string.isalpha():
        surname = string.capitalize()
        print(f"Surname entered: {surname}")
        break
    else:
        print("only characters please! ")


print(f"+{28*'-'}+")
print(f"|{(name+ ' ' + surname).center(28)}|")
print(f"+{28*'-'}+")