def digits_print(number):
    third = number % 10
    number = number // 10
    second = number % 10
    first = number // 10
    print(f"1st digit: {first}")
    print(f"2nd digit: {second}")
    print(f"3rd digit: {third}")


def digits(number):
    if number < 100 or number > 999:
        return None
    else:
        third = number % 10
        number = number // 10
        second = number % 10
        first = number // 10
        return first, second, third

digits_print(352)

f, s, t = digits(352)
print(f)
print(s)
print(t)

print(digits(44))