class Author:
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email


class Book:
    def __init__(self, title, authors, price, copies):
        self.title = title
        self.authors = authors
        self.price = price
        self.copies = copies

    def print_full_title(self):
        authors_names = [author.full_name for author in self.authors]
        print("'" + self.title + "' by ", end="")
        print(", ".join(authors_names))

    def add_author(self, author):
        self.authors.append(author)


p1 = Author("Bob Paterson", "bob@pcookbook.com")
p2 = Author("James McConan", "james@pcookbook.com")
b = Book("The Ultimate Python Cookbook", [p1,p2], 18.25, 43)
b.print_full_title()

b.add_author(Author("Tom Rossbow", "tom@pcookbook.com"))
b.print_full_title()