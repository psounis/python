# multiple.inheritance.py
class Base1:
    def __init__(self, b1_attr):
        self.b1_attr = b1_attr


class Base2:
    def __init__(self, b2_attr):
        self.b2_attr = b2_attr


class Derived(Base1, Base2):
    def __init__(self, b1_attr, b2_attr, d_attr):
        Base1.__init__(self, b1_attr)
        Base2.__init__(self, b2_attr)
        self.d_attr = d_attr


d = Derived(1,2,3)
print(f"{d.b1_attr}, {d.b2_attr}, {d.d_attr}")