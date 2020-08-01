class Teacher:
    def __init__(self, first_name="", surname="", teacher_id=-1):
        self.first_name = first_name
        self.surname = surname
        self.teacher_id = teacher_id

    def from_dict(self, teacher_dict):
        self.first_name = teacher_dict["first_name"]
        self.surname = teacher_dict["surname"]
        self.teacher_id = teacher_dict["teacher_id"]

    def to_dict(self):
        teacher_dict = {"first_name": self.first_name,
                        "surname": self.surname,
                        "teacher_id":self.teacher_id}
        return teacher_dict

    def print_teacher(self):
        print(f"Name   : {self.first_name}")
        print(f"Surname: {self.surname}")
        print(f"id     : {self.teacher_id}")