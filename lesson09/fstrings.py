print(f"With a result: {1+4}")
x = 3
print(f"For debugging: {x=}")
mult_line = (
  f"multiline: {x} value\n"
  f"multiline: {x*x} square"
)
print(mult_line)
print(f"A float with 2 decimals: {1/3:.2}|")
print(f"A float with width 6: {1/4:6}|")
print(f"A float with width 6 and 2 decimals: {1/3:6.2}|")
print(f"An integer(hexadecimal): {155:x}")
print(f"An integer(octal): {155:o}")
print(f"An integer(scientific): {155:e}")