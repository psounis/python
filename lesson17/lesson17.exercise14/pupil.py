class Pupil:
    def __init__(self, first_name="", last_name="", fathers_name="",
                 age=-1, class_name="", id_number=None, pupil_id=-1):
        self.first_name = first_name
        self.last_name = last_name
        self.fathers_name = fathers_name
        self.age = age
        self.class_name = class_name
        self.id_number = id_number
        self.pupil_id = pupil_id

    def from_dict(self, pupil_dict):
        self.first_name = pupil_dict["first_name"]
        self.last_name = pupil_dict["last_name"]
        self.fathers_name = pupil_dict["fathers_name"]
        self.age = pupil_dict["age"]
        self.class_name = pupil_dict["class_name"]
        if "id_number" in pupil_dict:
            self.id_number = pupil_dict["id_number"]
        self.pupil_id = pupil_dict["pupil_id"]

    def to_dict(self):
        pupil_dict = {"first_name": self.first_name,
                      "last_name": self.last_name,
                      "fathers_name": self.fathers_name,
                      "age": self.age,
                      "class_name": self.class_name,
                      "pupil_id": self.pupil_id}
        if self.id_number is not None:
            pupil_dict["id_number"] = self.id_number
        return pupil_dict

    def __str__(self):

        st =  f"\nName          : {self.first_name}"
        st += f"\nLast Name     : {self.last_name}"
        st += f"\nFather's Name : {self.fathers_name}"
        st += f"\nAge           : {self.age}"
        st += f"\nClass         : {self.class_name}"
        if self.id_number is not None:
            st += f"\nID card number: {self.id_number}"
        return st
