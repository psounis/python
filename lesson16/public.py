# public.py
class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.hunger = hunger

    def express(self):
        if self.hunger > 5:
            print("Moooooowwwwwwwwww")
        else:
            print("Mowww")


molly = Cow(100, 5)
print(molly.hunger)
print(molly.weight)
molly.express()