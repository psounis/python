string = "You have to die a few times before you can really live."
print("split(by blanks): " + str(string.split()))
print("split(by a's): " + str(string.split("a")))
print("split(by blanks): " + str(string.split(" ", 2)))
print("rsplit(by blanks): " + str(string.rsplit(" ", 2)))
print("partition(by 'few'): " + str(string.partition("few")))
print("rpartition(by 'r'): " + str(string.rpartition("r")))

mult_line = """Some lose all mind and become soul, insane.
some lose all soul and become mind, intellectual.
some lose both and become accepted"""
print("splitlines: " + str(mult_line.splitlines()))