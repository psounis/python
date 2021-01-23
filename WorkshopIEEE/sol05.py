movie=["lot1","lot2","lot3","batman"]
fmovie=input("dwse mia agapimeni:")
if fmovie in movie:
    print(" Yparxei hdh")
else:
    movie.append(fmovie)
    movie.sort()
    print(movie)