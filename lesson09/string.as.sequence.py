string = "Sample String"
print((string + " ") * 3)           # mult
print(string[1])                    # indexing
print(string[1:4] + string[-4:-1])  # slicing
print(len(string))                  # length
print(max("sample"))                # max
print(min("String"))                # min
print(string.index("am"))           # searching
print(string.count("S"))            # counting
# str[2] = "c"  not working..
new_str = string[:2] + "c" + string[3:]
print(new_str)