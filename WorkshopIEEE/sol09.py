class Dog:
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.mood = 5

    def eat(self):
        self.mood += 1
        if self.mood > 10:
            self.mood = 10

    def bark(self):
        if self.mood > 5:
            print("Woof Woof Woof")
        else:
            print("Woof")

    def walk(self):
        self.eat()


piko = Dog("Piko", 10, "Terrier")
piko.bark()
piko.walk()
piko.bark()
piko.walk()
piko.bark()
piko.eat()
piko.bark()

lassie = Dog("Lassie", 30, "Colley")
