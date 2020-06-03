
for a in range(1,20+1):
    for b in range(1, 20+1):
        for c in range(1, 20+1):
            if a**2 + b**2 == c**2:
                print("(" + str(a)+","+str(b)+","+str(c)+")")