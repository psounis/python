import unittest
from teacher import Teacher


class TeacherTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bush = Teacher("George", "Bush")
        self.clinton = Teacher("Bill", "Clinton", 1001)

    def test_from_dict(self):
        dict_arg = {
             "first_name": "George",
             "surname": "Bush",
             "teacher_id": -1
        }
        t = Teacher()
        t.from_dict(dict_arg)
        self.assertEqual(self.bush.first_name, t.first_name)
        self.assertEqual(self.bush.surname, t.surname)
        self.assertEqual(self.bush.teacher_id, t.teacher_id)

    def test_to_dict(self):
        dict_arg = {
             "first_name": "George",
             "surname": "Bush",
             "teacher_id": -1
        }

        self.assertEqual(self.bush.to_dict()["first_name"], dict_arg["first_name"])
        self.assertEqual(self.bush.to_dict()["surname"], dict_arg["surname"])
        self.assertEqual(self.bush.to_dict()["teacher_id"], dict_arg["teacher_id"])
