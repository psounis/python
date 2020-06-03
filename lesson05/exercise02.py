cnt = 1
s = 0
while cnt <= 10:
    user_input = int(input("Give " + str(cnt) + "th number: "))
    cnt += 1
    s += user_input

print("sum=" + str(s))
