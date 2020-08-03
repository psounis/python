class Point3D:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __add__(self, other):
        new_point = Point3D()
        new_point.x = self.x + other.x
        new_point.y = self.y + other.y
        new_point.z = self.z + other.z
        return new_point

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        return None

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value

a = Point3D(1,1,1)
b = Point3D(2,2,2)
print(a+b)
c = a + b
print(c)
print(a, id(a))
a = a + b
print(a, id(a))
a += b
print(a, id(a))
a[0]=7
print(a)