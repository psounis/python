from random import seed
from random import randrange
from datetime import datetime  # all 3 at the beginning

seed(datetime.now())  # once, before randint call

words = [
"retreat",
"page",
"integrated",
"coincidence",
"mouse",
"trait",
"encourage",
"flour",
"fast",
"attachment",
"idea",
"undress",
"quota",
"miss",
"motif"
]

hidden_word = words[randrange(len(words))]
print(hidden_word)

guessed_letters = []
max_rounds = 10
for round in range(1, max_rounds+1):
    print(f"ROUND {round}")
    while True:
        letter = input("give a letter: ").lower()

        if len(letter)!=1:
            print("Error. Please give ONE letter!!")
        elif not letter.isalpha():
            print("Error. Please write letters!")
        elif letter in guessed_letters:
            print("You have already typed this letter!")
        else:
            break




    guessed_letters.append(letter)

    print(f"Letter {letter} exists {hidden_word.count(letter)} in hidden word.")

    found = True
    for char in hidden_word:
        if char in guessed_letters:
            print(char, end="")
        else:
            print("_", end="")
            found = False
    print("")

    if found:
        print("Success! You 've found it!")
        break
else:
    print("Failure! Maximum rounds reached!")
    print("The hidden word was: " + hidden_word)