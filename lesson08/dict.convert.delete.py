a_list = [("name", "Natasha Romanoff"), ("alias", "Black Widow")]
hero = dict(a_list)
hero["ability"] = "hand-to-hand combat"
print(hero)
hero.pop("name")
print(hero)
hero.clear()
print(hero)