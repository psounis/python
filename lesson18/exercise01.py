class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height


class Horse(Animal):
    def __init__(self, weight, height, color, tail):
        super().__init__(weight, height)
        self.color = color
        self.tail = tail


class Dog(Animal):
    def __init__(self, weight, height, db):
        super().__init__(weight, height)
        self.db = db

    def bark(self):
        print("Woof woof")


class Doberman(Dog):
    def __init__(self, weight, height, db):
        super().__init__(weight, height, db)

    def run(self):
        print("Doberman is running")


class Bulldog(Dog):
    def __init__(self, weight, height, db, ear_length):
        super().__init__(weight, height, db)
        self.ear_length = ear_length

    def sleep(self):
        print("Bulldog is sleeping")


dolly = Horse(300,2,"white",1)
tobie = Doberman(50,1.1,8)
buddy = Bulldog(70,1,9,0.4)

print(dolly.color)
tobie.bark()
tobie.run()
tobie.bark()
buddy.bark()
buddy.sleep()
buddy.sleep()