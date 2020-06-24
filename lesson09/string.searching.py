string = "Some people never go crazy. What truly horrible lives they must lead."
print("startswith: " + str(string.startswith("Some")))
print("startswith with bounds: " + str(string.startswith("people", 5)))
print("startswith with bounds: " + str(string.startswith("people", 5,8)))
print("endswith: " + str(string.endswith("people",0,11)))
print("find: " + str(string.find("crazy")))
print("position(s) of \"o\": ", end="")
pos = -1
lpos = string.rfind("o")
while pos != lpos:
    pos = string.find("o", pos+1)
    print(pos, end=" ")

print("\nreplace: " + string.replace("o","0",3))