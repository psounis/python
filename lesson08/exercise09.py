from random import seed
from random import randrange
from datetime import datetime  # all 3 at the beginning

seed(datetime.now())  # once, before randint call

round = 0
score = [0, 0] # Player, computer
history = []
while True:
    round += 1
    print("Round " + str(round))

    # Eisodos xristi
    player_input = input("Choose: ")
    while player_input not in ["rock", "scissors", "paper"]:
        print("Wrong input. Choices: rock, scissors, paper")
        player_input = input("Choose: ")

    # Epilogi ipologisti
    computer_random = randrange(3)
    if computer_random == 0:
        computer_choice = "rock"
    elif computer_random == 1:
        computer_choice = "scissors"
    else:
        computer_choice = "paper"

    # Elegxos toy poios nikise
    if player_input == "rock":
        if computer_choice == "rock":
            winner = "no winner"
        elif computer_choice == "paper":
            winner = "computer"
        else:
            winner = "player"
    elif player_input == "paper":
        if computer_choice == "rock":
            winner = "player"
        elif computer_choice == "paper":
            winner = "no winner"
        else:
            winner = "computer"
    else: # player_input == scissors
        if computer_choice == "rock":
            winner = "computer"
        elif computer_choice == "paper":
            winner = "player"
        else:
            winner = "no winner"

    # Diorthosi tou skor

    if winner == "player":
        score[0] += 1
    elif winner == "computer":
        score[1] += 1

    # enimerwsi tou istorikou
    history.append("Round " + str(round) + ": Player: " + player_input + ", Computer: " + computer_choice + ", Score: " + str(score[0]) + "-" + str(score[1]))

    # Ektypwsi toy nikiti kai tou skor

    print("Computer picks: " + computer_choice)
    print("Player-Computer: " + str(score[0]) + "-" + str(score[1]))

    if score[0] == 3:
        print("Player wins! ")
        print("")
        for history_item in history:
            print(history_item)
        break
    elif score[1] == 3:
        print("Computer wins! ")
        print("")
        for history_item in history:
            print(history_item)
        break

    print("====================\n")