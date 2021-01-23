day = "Sunday"
tired = True

if day == "Saturday":
    print("I read a bit")
elif day == "Sunday":
    if tired:
        print("I won't study at all")
    else:
        print("I will study a lot")
else:
    print("I will study")