class Flat:
    def __init__(self):
        self.people = 0


class Storey:
    def __init__(self, number_flats):
        self.flats = [Flat() for _ in range(number_flats)]


class Building:
    def __init__(self, number_storeys, number_flats):
        self.storeys = [Storey(number_flats) for _ in range(number_storeys)]

    def add_people(self, storey, flat, people):
        self.storeys[storey].flats[flat].people += people

    def print_people(self):
        for i in range(len(self.storeys)):
            for j in range(len(self.storeys[i].flats)):
                print(f"Storey {i}, Flat {j}: {self.storeys[i].flats[j].people} people")


b = Building(3,4)
b.add_people(0,1,2)
b.print_people()