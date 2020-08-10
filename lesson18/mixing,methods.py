class HasMethod1(object):
    def method(self):
        return 1

class HasMethod2(object):
    def method(self):
        return 2

class UsesMethod10(object):
    def usesMethod(self):
        return self.method() + 10

class UsesMethod20(object):
    def usesMethod(self):
        return self.method() + 20

class C1_10(HasMethod1, UsesMethod10): pass
class C1_20(HasMethod1, UsesMethod20): pass
class C2_10(HasMethod2, UsesMethod10): pass
class C2_20(HasMethod2, UsesMethod20): pass

print(C1_10().usesMethod())
print(C1_20().usesMethod())
print(C2_10().usesMethod())
print(C2_20().usesMethod())

# Nothing prevents implementing the method
# on the base class like in Definition 1:

class C3_10(UsesMethod10):
    def method(self):
        return 3

print(C3_10().usesMethod())