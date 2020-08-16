filename = "filename.txt"

try:
    with open(filename) as f:
        st = f.read()
except FileNotFoundError:
    print(f"File '{filename}' does not exist.")
    choice = input("Do you want to create the file? (y/n):")
    if choice == "y":
        with open(filename, "w") as f:
            pass


