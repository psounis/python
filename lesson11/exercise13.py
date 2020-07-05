from random import seed
from random import randrange
from datetime import datetime  # all 3 at the beginning

# globals

kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10,"jack", "queen", "king"}

deck = set()


# functions

def hand_value(hand):
    s = 0
    ace = False
    for card in hand:
        n = card[1]
        if n == "jack" or n == "queen" or n == "king":
            s += 10
        elif n == "ace":
            ace = True
            s += 1
        else:
            s += n

    if ace:
        if s + 10 <= 21:
            s += 10

    return s


def player(hand):
    hand.add(deck.pop())
    hand.add(deck.pop())

    while True:
        print(hand)
        choice = input("h-Hit or s-Stand: ")
        if choice == "h":
            hand.add(deck.pop())
            value = hand_value(hand)
            if value >= 21:
                return value
        elif choice == "s":
            return hand_value(hand)


def computer(value_player, hand):
    hand.add(deck.pop())
    hand.add(deck.pop())

    while True:
        value = hand_value(hand)

        if value >= 21:
            return value
        elif value >= value_player:
            return value
        else:
            hand.add(deck.pop())


# main

def main():
    global deck
    seed(datetime.now())  # once, before randint call
    rounds = 1
    score = [0, 0]

    while True:
        print("=" * 15)
        print("Round " + str(rounds))
        print("=" * 15)

        deck = {(k, n) for k in kind for n in number}

        player_hand = set()
        player_value = player(player_hand)

        print(f"{player_hand} with value: {player_value}")
        if player_value == 21:
            print("You won!")
            result = "player"
        elif player_value > 21:
            print("You lost!")
            result = "computer"
        else:
            print("Computer plays")
            computer_hand = set()
            computer_value = computer(player_value, computer_hand)
            print(f"{computer_hand} with value: {computer_value}")
            if computer_value > 21:
                print("You won!")
                result = "player"
            else:
                print("You lose!")
                result = "computer"

        if result == "player":
            score[0] += 1
        else:
            score[1] += 1

        print(f"Score: Player:{score[0]} - Computer:{score[1]}")
        choice = input("Do you want to play again(y-yes, n-no):")
        if choice == "n":
            print("Bye bye!!")
            break

        rounds += 1


main()
