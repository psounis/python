from character import Character

class Tank(Character):
    def __init__(self, character_name, equipment, attack_speed=2, delay=0):
        super().__init__(character_name, equipment, attack_speed, delay)
        self.attack_range = (20, 30)
        self.max_health = self.max_health * 2
        self.health = self.max_health
