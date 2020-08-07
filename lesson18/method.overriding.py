# method.overriding.py
class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.hunger = hunger

    def express(self):
        if self.hunger > 5:
            print("Moooooowwwwwwwwww")
        else:
            print("Mowww")


class TexasLonghorn(Cow):
    def __init__(self, weight, hunger, horn_length):
        super().__init__(weight, hunger)
        self.horn_length = horn_length

    def express(self):
        if self.hunger > 5:
            print("MEEoooEEEwwwwwwwww")
        else:
            print("MEoEwww")

molly = Cow(500, 10)
molly.express()

bob = TexasLonghorn(400,20,0.50)
bob.express()
print(f"Bob's horns are {bob.horn_length} meters long")
print(f"Bob's weight={bob.weight}, hunger={bob.hunger}, horn_length={bob.horn_length}")