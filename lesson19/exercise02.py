def get_integer():
    while True:
        try:
            user_input = input("Give integer: ")

            if user_input[0] == "-":
                st = user_input[1:]
                if st == "":
                    raise ValueError("No digits entered!")
                elif not st.isdigit():
                    raise ValueError("Wrong Input. Only digits please!")
                x = -int(st)
            else:
                st = user_input
                if st == "":
                    raise ValueError("No digits entered!")
                elif not st.isdigit():
                    raise ValueError("Wrong Input. Only digits please!")
                x = int(st)

        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
        else:
            return x


print(get_integer())