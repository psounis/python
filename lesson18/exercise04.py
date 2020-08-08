# protected.py
class Base:
    def __init__(self):
        self.__bpr_attr = 1


class Derived(Base):
    def __init__(self):
        super().__init__()


d = Derived()
print(d._Base__bpr_attr)
print(d.__bpr_attr)