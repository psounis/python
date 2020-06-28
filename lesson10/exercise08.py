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


while True:
    print("\n===============")
    print("     MENU ")
    print("1 - Create Pupil")
    print("2 - Print")
    print("3 - Update Pupil")
    print("4 - Delete Pupil")
    print("5 - Exit")
    choice = int(input("Pick one: "))

    if choice==1:
        print("NEW PUPIL")
        print("===========")
        name = input("Give name: ")
        surname = input("Give surname: ")
        fathers_name = input("Give father's name: ")

        stop=False
        for p in pupils:
            if name==p["name"] and surname==p["surname"] and fathers_name==p["fathers_name"]:
                print("This pupil already exists.")
                ch = input("Do you want to continue? (y-yes, n-no): ")
                if ch=="n":
                    stop = True
                    break
        if stop:
            continue

        age = int(input("Give age: "))
        pupil_class = int(input("Give class: "))
        id_card = input("Does he/she has an id card: (y-true, n-false): ")
        if id_card=="y":
            id_number = input("Give id card number: ")

        pupil = {}
        pupil["name"]=name
        pupil["surname"]=surname
        pupil["fathers_name"]=fathers_name
        pupil["age"]=age
        pupil["class"]=pupil_class
        if id_card=="y":
            pupil["id_number"]=id_number

        ids = []
        for p in pupils:
            ids.append(p["id"])
        pupil["id"] = max(ids) + 1

        pupils.append(pupil)


        print("NEW PUPIL")
        print(f"Name: {pupil['name']}")
        print(f"Surname: {pupil['surname']}")
        print(f"Father's Name: {pupil['fathers_name']}")
        print(f"Age: {pupil['age']}")
        print(f"Class: {pupil['class']}")
        if pupil["id_number"]:
            print(f"ID card number: {pupil['id_number']}")

    elif choice==2:
        pass
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("Bye bye!")
        break
