def input_float():
    while True:
        data = input("Give an float: ").strip()
        if "." in data:
            parts = data.split(".")
            if len(parts) > 2:
                print("Only one dot at most please.")
            elif parts[0].isdigit() and parts[1].isdigit():
                return float(data)
            else:
                print("Only digits please.")
        else: # . not in data
            if data.isdigit():
                return float(data)
            else:
                print("Only digits please. ")


print(input_float())