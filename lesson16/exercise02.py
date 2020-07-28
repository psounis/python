class Philosopher:
    def __init__(self, full_name, era, books, school):
        self.full_name = full_name
        self.era = era
        self.books = books
        self.school = school
        self.disputed_books = []


plato = Philosopher("Plato", "Ancient Greece", ["The Republic", "Phaedo"], "Platonism")
baruch = Philosopher("Baruch Spinoza", "Modern Netherlands", ["Ethics", "Political Treatise"], "Modernism")

print(baruch.disputed_books)