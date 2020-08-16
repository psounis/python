class ValueTooSmallError(Exception):
    def __init__(self, message):
        self.message = message


class ValueTooLargeError(Exception):
    def __init__(self, message):
        self.message = message


class NotMultipleOfFiveError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"{self.val} is not multiple of 5"


def get_integer_con():
    while True:
        try:
            user_input = input("Give integer: ")

            if user_input[0] == "-":
                st = user_input[1:]
                if st == "":
                    raise ValueError("No digits entered!")
                elif not st.isdigit():
                    raise ValueError("Wrong Input. Only digits please!")
                else:
                    raise ValueTooSmallError("Value must be >= 100.")
            else:
                st = user_input
                if st == "":
                    raise ValueError("No digits entered!")
                elif not st.isdigit():
                    raise ValueError("Wrong Input. Only digits please!")
                x = int(st)
                if x < 100:
                    raise ValueTooSmallError("Value must be >= 100.")
                elif x > 200:
                    raise ValueTooLargeError("Value must be <= 200.")
                elif x % 5 != 0:
                    raise NotMultipleOfFiveError(x)

        except (ValueTooSmallError, ValueTooLargeError, NotMultipleOfFiveError) as e:
            print(e)
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
        else:
            return x


print(get_integer_con())