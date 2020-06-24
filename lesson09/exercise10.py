for i in range(10000):
    if i%50==0:
        print(f"\n{i}-{i+49}: ", end="")
    print(chr(i), end="")
