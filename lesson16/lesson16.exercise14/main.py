from character import Character
from arena import Arena
from random import randrange, seed
from datetime import datetime


def main():
    seed(datetime.now())

    orcs = [Character("Orc-" + str(i+1),2,randrange(4)) for i in range(5)]
    night_elves = [Character("Night-Elf-" + str(i + 1), 3, randrange(3)) for i in range(3)]

    a = Arena(orcs, night_elves)
    a.play()


main() 