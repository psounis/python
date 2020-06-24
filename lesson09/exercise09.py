string = "Hello!"
integer = 5
fl = 3.14

print(string + " " + str(integer) + " " + str(fl))
print(f"{string} {integer} {fl}")
print("%s %d %f" % (string, integer, fl))
print("{} {} {}".format(string, integer, fl))