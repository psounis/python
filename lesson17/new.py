class A:
    def __new__(cls):
        print("A.__new__ called")
        return super(A, cls).__new__(cls)
    def __init__(self):
        print("A.__init__ called")

A()
