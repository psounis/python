from teachers import Teachers
from pupils import Pupils


class Lesson:
    def __init__(self, lesson_name="", lesson_id=-1):
        self.lesson_name = lesson_name
        self.teacher_ids = []
        self.pupil_ids = []
        self.lesson_id = lesson_id

    def from_dict(self, lesson_dict):
        self.lesson_name = lesson_dict["lesson_name"]
        self.teacher_ids = lesson_dict["teacher_ids"]
        self.pupil_ids = lesson_dict["pupil_ids"]
        self.lesson_id = lesson_dict["lesson_id"]

    def to_dict(self):
        lesson_dict = {"lesson_name": self.lesson_name,
                       "teacher_ids": self.teacher_ids,
                       "pupil_ids": self.pupil_ids,
                       "lesson_id": self.lesson_id
                       }

        return lesson_dict

    def print_lesson_details(self, teachers, pupils):
        print(f"LESSON: {self.lesson_name}")
        print("=========")
        print("TEACHERS: ")
        for teacher_id in self.teacher_ids:
            teacher = teachers.read_teacher(teacher_id)
            print(f"{teacher.first_name} {teacher.surname}")
        print("STUDENTS: ")
        for pupil_id in self.pupil_ids:
            pupil = pupils.search_pupil_by_id(pupil_id)
            print(f"{pupil.first_name} {pupil.last_name}")

