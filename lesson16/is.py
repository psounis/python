class MyClass:
    def __init__(self, x):
        self.x = x


o1 = MyClass(2)
o2 = MyClass(3)
o3 = o2

print(id(o1), id(o2), id(o3))
print(o1 is o2)
print(o2 is o3)
print("======")

print([1,2] is [1,2])
print([1,2] == [1,2])

o1 = MyClass(1)
o2 = MyClass(1)
print(o1 is o2)
print(o1 == o2) # doesn't work right (we 'll fix it later)
print("======")

print(isinstance([1,2],list))
print(isinstance(o1,MyClass))
print(isinstance(o1,float))
print(isinstance([1,2],(list,int)))
