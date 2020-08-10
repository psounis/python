# mixin.py
class ComparableMixin:
    """This class has methods which use `<=` and `==`,
    but this class does NOT implement those methods."""
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return self <= other and (self != other)
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return self == other or self > other

class Integer(ComparableMixin):
    def __init__(self, i):
        self.i = i
    def __le__(self, other):
        return self.i <= other.i
    def __eq__(self, other):
        return self.i == other.i

print(Integer(3)<=Integer(4))
print(Integer(3)<Integer(4))