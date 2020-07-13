def print_full_name(first_name, surname, fathers_name):
    print(f"{first_name} {fathers_name[0]}. {surname}")


print_full_name("Jack", "Bauer", "Philip")
print_full_name("Jack", fathers_name="Philip", surname="Bauer")