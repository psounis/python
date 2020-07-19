pupils = [
    {
        "id": 1001,
        "name": "John",
        "surname": "Doe",
        "fathers_name": "Michael",
        "age": 11,
        "class": 1,
        "id_number": "AN123949"
    },
    {
        "id": 1002,
        "name": "Mary",
        "surname": "Poppins",
        "fathers_name": "Chris",
        "age": 10,
        "class": 3,
        "id_number": "AE123981"
    },
    {
        "id": 1003,
        "name": "John",
        "surname": "Wick",
        "fathers_name": "Chiwetel",
        "age": 7,
        "class": 6,
    }
]



# functions

def print_pupil(pupil):
    print(f"Name          : {pupil['name']}")
    print(f"Surname       : {pupil['surname']}")
    print(f"Father's Name : {pupil['fathers_name']}")
    print(f"Age           : {pupil['age']}")
    print(f"Class         : {pupil['class']}")
    if "id_number" in pupil:
        print(f"ID card number: {pupil['id_number']}")


def next_id():
    ids = []
    for p in pupils:
        ids.append(p["id"])
    return max(ids) + 1


def create_pupil():
    name = input("Give name: ")
    surname = input("Give surname: ")
    fathers_name = input("Give father's name: ")

    for p in pupils:
        if name == p["name"] and surname == p["surname"] and fathers_name == p["fathers_name"]:
            print("This pupil already exists.")
            ch = input("Do you want to continue? (y-yes, n-no): ")
            if ch == "n":
                return None

    age = int(input("Give age: "))
    pupil_class = int(input("Give class: "))
    id_card = input("Does he/she has an id card: (y-true, n-false): ")
    if id_card == "y":
        id_number = input("Give id card number: ")

    pupil = {}
    pupil["name"] = name
    pupil["surname"] = surname
    pupil["fathers_name"] = fathers_name
    pupil["age"] = age
    pupil["class"] = pupil_class
    if id_card == "y":
        pupil["id_number"] = id_number

    pupil["id"] = next_id()

    pupils.append(pupil)
    return pupil


def search_pupil_by_id(pupil_id):
    for pupil in pupils:
        if pupil_id == pupil["id"]:
            return pupil
    return None


def search_pupil_by_surname(surname):
    match_pupils = []
    for pupil in pupils:
        if surname == pupil["surname"]:
            match_pupils.append(pupil)
    return match_pupils


def pupil_update(pupil):
    print_pupil(pupil)
    print("=" * 15)
    print("1-name")
    print("2-surname")
    print("3-father's name")
    print("4-age")
    print("5-class")
    print("6-id number")
    print("=" * 15)
    update_choice = int(input("Pick something to update: "))
    if update_choice == 1:
        pupil["name"] = input("Give new name: ")
    elif update_choice == 2:
        pupil["surname"] = input("Give new surname: ")
    elif update_choice == 3:
        pupil["fathers_name"] = input("Give new father's name: ")
    elif update_choice == 4:
        pupil["age"] = input("Give new age: ")
    elif update_choice == 5:
        pupil["class"] = input("Give new class: ")
    elif update_choice == 6:
        pupil["id_number"] = input("Give new id number: ")

    print("=" * 15)
    print_pupil(pupil)
    print("Pupil updated! ")


def delete_pupil_by_id(id):
    for i in range(len(pupils)):
        if id == pupils[i]["id"]:
            pupils.pop(i)
            return


def print_pupils_details():
    for pupil in pupils:
        print("=" * 15)
        print_pupil(pupil)


def print_pupils_names():
    for pupil in pupils:
        print(f"{pupil['name']} {pupil['fathers_name'][0]}. {pupil['surname']}")

