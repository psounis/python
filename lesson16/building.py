class Storey:
    def __init__(self):
        self.people = 0


class Building:
    def __init__(self, number_storeys):
        self.storeys = [Storey() for _ in range(number_storeys)]

    def add_people(self, storey, people):
        self.storeys[storey].people += people

    def print_people(self):
        for i in range(len(self.storeys)):
            print(f"Storey {i}: {self.storeys[i].people} people")


b = Building(3)
b.add_people(0,2)
b.print_people()