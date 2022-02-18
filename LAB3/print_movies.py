def print_films(moves):
    for i in moves:
        print("Name - ",i.get("name"))
        print("IMDB rating - ", i.get("imdb"))
        print("Category - ", i.get("category"))
        print()