class Animal:
    def make_sound(self):
        print("")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


class HimalayanCat(Cat):
    def make_sound(self):
        super().make_sound()
        print("Miouw Miouw")


class Dog(Animal):
    def make_sound(self):
        print("Woof woof")


class Doberman(Dog):
    pass


class KingDoberman(Doberman):
    def make_sound(self):
        super().make_sound()
        print("WOOAAAAAAAFFF")


Animal().make_sound()
Cat().make_sound()
HimalayanCat().make_sound()
Dog().make_sound()
Doberman().make_sound()
KingDoberman().make_sound()