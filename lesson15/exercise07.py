def merge(filename1, filename2, filename):
    with open(filename, "w") as f:
        with open(filename1) as g:
            contents = g.read()
        f.write(contents)

        with open(filename2) as g:
            contents = g.read()
        f.write(contents)


merge("test.txt", "test2.txt", "test4.txt")
