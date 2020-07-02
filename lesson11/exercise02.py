def favorite_author(author):
    if "Tolkien" in author:
        for _ in range(500):
            print("Tolkien is the best!!")
    else:
        print(author + "is good!")


favorite_author("J.R.R. Tolkien")
favorite_author("Stephen King")