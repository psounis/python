favorite_movies = ["Movie 1", "Movie 2", "Movie 3", "Movie 4"]

new_movie = input("Dwse kainourgia tainia: ")

if new_movie in favorite_movies:
    print("Yparxei hdh. Den egine apothikeusi")
else:
    favorite_movies.append(new_movie)
    favorite_movies.sort()
    print(favorite_movies)
    print(len(favorite_movies))
