string = "Hello "
concatenation = string + string
print(f"Concatenation(+): {concatenation}")
multiplication = string * 5
print(f"Multiplication(*): {multiplication}")
string += "World!" # string = string + "World!"
print(f"Increment: {string}")
print(f"Char in string: 'W' in {string}: {'W' in string}")
print(f"Char not in string: 'W' not in {string}: {'W' not in string}")
comparison = "abc" < "abd" # also: >, <=, >=
print(f"Comparison: {comparison}")
equality = "aa" == "AA".lower() # also not equal: !=
print(f"Equality: {equality}")