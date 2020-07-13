# positional.after.keyword.args.py
def print_full_name(first_name, surname, fathers_name):
    print(f"{first_name} {fathers_name[0]}. {surname}")


print_full_name(surname="Bauer", first_name="Jack", "Philip")