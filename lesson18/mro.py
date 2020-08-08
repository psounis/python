# mro.py
class A:
    pass

class B1(A):
    pass

class B2(A):
    pass

class D(B1, B2):
    pass

print(D.mro())
