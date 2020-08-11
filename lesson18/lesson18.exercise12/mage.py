from character import Character
from random import randrange


class Mage(Character):
    def __init__(self, character_name, equipment, attack_speed=2, delay=0):
        super().__init__(character_name, equipment, attack_speed, delay)
        self.attack_range = (8, 17)
        self.mana  = 100
        self.max_mana = 100

    def end_round(self):
        super().end_round()
        self.mana = self.mana + 1 if self.mana + 1 <= self.mana else self.max_mana

    def lightning_spell(self):
        self.mana -= 55
        return randrange(30, 50)

    def attack(self):
        self.delay = self.max_delay - self.attack_speed
        if self.mana >= 55:
            return self.lightning_spell()
        else:
            return round(randrange(self.attack_range[0], self.attack_range[1]) * self.equipment.sword)
