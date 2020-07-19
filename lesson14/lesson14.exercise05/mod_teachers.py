teachers = [
    {
        "id": 1001,
        "name": "Severus",
        "surname": "Snape",
    },
    {
        "id": 1002,
        "name": "Charles",
        "surname": "Xavier",
    },
    {
        "id": 1003,
        "name": "Sergio",
        "surname": "Marquina",
    }
]


def next_id():
    ids = []
    for t in teachers:
        ids.append(t["id"])
    return max(ids) + 1


def create_teacher(first_name, surname):
    for teacher in teachers:
        if teacher["name"] == first_name and teacher["surname"] == surname:
            print("Error. Teacher already exists! ")
            return None

    t = {"name": first_name, "surname": surname, "id": next_id()}
    teachers.append(t)
    return t


def read_teacher(teacher_id):
    for teacher in teachers:
        if teacher_id == teacher["id"]:
            return teacher
    else:
        return None


def update_teacher(teacher_id, key, value):
    for teacher in teachers:
        if teacher_id == teacher["id"]:
            teacher[key] = value
            return


def delete_teacher(teacher_id):
    for i in range(len(teachers)-1):
        if teacher_id == teachers[i]["id"]:
            teachers.pop(i)
            return


def print_teacher(teacher):
    print(f"Name   : {teacher['name']}")
    print(f"Surname: {teacher['surname']}")
    print(f"id     : {teacher['id']}")