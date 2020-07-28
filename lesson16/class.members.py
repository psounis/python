# class.members.py
class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.hunger = hunger


molly = Cow(500, 10)
print(type(molly))
print(molly.hunger)