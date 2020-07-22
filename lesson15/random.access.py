int_size = 4
with open("binary.dat", "rb+") as f:
    while True:
        print(f"Current cursor position = {f.tell()}")
        print("1-read")
        print("2-write")
        print("3-exit")
        choice = int(input("Choose: "))

        if choice == 1:
            pos = int(input("Give position(0-3) to read: "))
            f.seek(int_size*pos, 0)
            b = f.read(int_size)
            print(f"value in pos {pos} = {int.from_bytes(b, byteorder='big')}")
        elif choice == 2:
            pos = int(input("Give position(0-3) to write: "))
            f.seek(int_size*pos, 0)
            val = int(input("Give new value: "))
            f.write(val.to_bytes(int_size, byteorder='big'))
            print(f"value in pos {pos} changed to {val}")
        else:
            break
