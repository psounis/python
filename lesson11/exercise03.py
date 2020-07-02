def input_integer():
    while True:
        data = input("Give an integer: ").strip()
        if data.isdigit():
            return int(data)
        else:
            print("Only digits please. ")

print(input_integer())