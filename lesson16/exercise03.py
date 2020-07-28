class Dog:
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.mood = 5

    def eat(self):
        self.mood += 1

    def bark(self):
        if self.mood > 5:
            print("Woof woof woof")
        else:
            print("Woof")

    def walk(self):
        self.mood += 1


piko = Dog("Piko", 10, "Terrier")
for _ in range(2):
    piko.bark()
    piko.walk()
piko.bark()
piko.eat()
piko.bark()