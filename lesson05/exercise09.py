hidden = 43

cnt = 0
max_guesses = 10
guess = int(input("Give a number: "))

while True:
    cnt += 1
    if cnt == max_guesses:
        print("You lose!")
        break

    if guess > hidden:
        print("It's smaller! ")
    elif guess < hidden:
        print("It's bigger! ")
    else:
        print("You've found it!")
        break

    guess = int(input("Give a number: "))

