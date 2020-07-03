# immutable.arguments.py
def f(arg):
    print(arg)
    arg="Change!"
    print(arg)

s = "Initial"
print(s)
f(s)
print(s)