from random import seed
from random import randrange
from datetime import datetime

# globals

score = [
    {
        "ones": -1,
        "twos": -1,
        "threes": -1,
        "fours": -1,
        "fives": -1,
        "sixes": -1,
    },
    {
        "ones": -1,
        "twos": -1,
        "threes": -1,
        "fours": -1,
        "fives": -1,
        "sixes": -1,
    }
]


# functions

def roll_dice(n):
    dice = []
    for i in range(n):
        dice += [randrange(1,6+1)]
    return sorted(dice)

def player_turn():
    dices_rolling = 5
    dice_kept = []

    for roll in range(3):
        dice = roll_dice(dices_rolling)
        print("-" * 15)
        print("Roll " + str(roll + 1) + "!")
        if roll in range(2):
            while True:
                print("Dice = " + str(dice))
                choice = input("Do you want to keep a die? (Type the number or 'n'): ")
                if choice == 'n':
                    break
                elif int(choice) not in dice:
                    print("There is no " + choice + "in your dice!")
                else:
                    dices_rolling -= 1
                    dice.remove(int(choice))
                    dice_kept += [int(choice)]
        else: # roll == 2
            dice_kept += dice

    print("Your dice is: " + str(dice_kept))
    return dice_kept


def translate_name(s):
    if s=="ones":
        return 1
    if s=="twos":
        return 2
    if s=="threes":
        return 3
    if s=="fours":
        return 4
    if s=="fives":
        return 5
    if s=="sixes":
        return 6

def player_picks(player, dice):
    print("You can store your dice as: ", end=", ")
    picks = []
    for key, value in score[player].items():
        if value == -1:
            print(key, end=", ")
            picks += [key]

    while True:
        choice = input("Type your choice: ")
        if choice not in picks:
            print("Wrong choice! ")
            continue
        else:
            key_val = translate_name(choice)
            score[player][choice] = dice.count(key_val) * key_val
            return


def print_card(player):
    print(f"PLAYER {player + 1} CARD")
    if score[player]["ones"] == -1:
        print("ones: ")
    else:
        print(f"ones: {score[player]['ones']}")

    if score[player]["twos"] == -1:
        print("twos: ")
    else:
        print(f"twos: {score[player]['twos']}")

    if score[player]["threes"] == -1:
        print("threes: ")
    else:
        print(f"threes: {score[player]['threes']}")

    if score[player]["fours"] == -1:
        print("fours: ")
    else:
        print(f"fours: {score[player]['fours']}")

    if score[player]["fives"] == -1:
        print("fives: ")
    else:
        print(f"fives: {score[player]['fives']}")

    if score[player]["sixes"] == -1:
        print("sixes: ")
    else:
        print(f"sixes: {score[player]['sixes']}")


def calculate_score(player):
    return sum(score[player].values())

# main


def main():
    seed(datetime.now())

    for round in range(1, 6+1):
        print("-" * 20)
        print(f"Round {round}!!")
        print("-" * 20)
        for player in range(2):
            print(f"Player {player + 1} ")
            print("-" * 15)
            print_card(player)
            print("-" * 15)
            dice = player_turn()
            player_picks(player, dice)

    print("\n\n")
    print_card(0)
    score1 = calculate_score(0)
    print(f"Player 1 score: {score1}")
    print_card(1)
    score2 = calculate_score(1)
    print(f"Player 2 score: {score2}")

    if score1 > score2:
        print("Player 1 wins!")
    elif score1 < score2:
        print("Player 2 wins!")
    else:
        print("Draw!!")


main()

