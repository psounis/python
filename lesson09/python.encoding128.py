for i in range(128):
    if i%10==0:
        print(f"\n{i}-{i+9}: ", end="")
    print(chr(i), end="")
