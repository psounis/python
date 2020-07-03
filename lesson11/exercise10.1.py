# immutable.arguments.py
def f(arg):
    print(arg)
    print(f"id arg={id(arg)}")
    arg="Change!"
    print(arg)
    print(f"id s={id(arg)}")

s = "Initial"
print(s)
print(f"id s={id(s)}")
f(s)
print(s)
print(f"id s={id(s)}")