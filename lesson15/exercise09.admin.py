import json

try:
    with open("users.json") as f:
        users = json.load(f)
except FileNotFoundError:
    users = []

while True:
    print("1-new user")
    print("2-exit")
    choice = int(input("Pick one: "))

    if choice == 1:
        user = {}
        user["full_name"] = input("Give full name: ")
        user["username"] = input("Give username: ")
        user["password"] = input("Give password: ")
        user["role"] = input("Give role (admin, user): ")
        users.append(user)
    elif choice == 2:
        with open("users.json", "w") as f:
            json.dump(users, f)
        break
