my_friends = ["a", "b", "c"]
guests = ["1", "2", "a", "4", "5", "6", "b", "8", "9", "10"]

cnt = 0
for friend in my_friends:
    if friend in guests:
       cnt += 1

if cnt < 2:
    print("I won't come")
else:
    print("I'll come")