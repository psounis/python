import json

teachers = []

def init_teachers_data():
    global teachers
    try:
        with open("teachers.json") as f:
            teachers = json.load(f)
    except FileNotFoundError:
        teachers = []


def save_teachers_data():
    with open("teachers.json", "w") as f:
        json.dump(teachers, f)


def next_id():
    if not teachers:
        return 1001
    else:
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