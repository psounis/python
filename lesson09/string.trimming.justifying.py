string = "   Factotum "
print("lstrip : |" + string.lstrip() + "|")
print("rstrip : |" + string.rstrip() + "|")
print("strip  : |" + string.strip() + "|")
print("ljust  : |" + string.strip().ljust(30) + "|")
print("rjust  : |" + string.strip().rjust(30) + "|")
print("center : |" + string.strip().center(30,"-") + "|")

string = "abcd"
print("zfill(2) : " + string.zfill(2))
print("zfill(10): " + string.zfill(10))