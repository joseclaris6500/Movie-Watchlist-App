import datetime
import database

menu = """Please select one of the following options:
(1) Add new movie
(2) View upcoming moves.
(3) View all movies.
(4) Watch a movie.
(5) View watched movies.
(6) Add user
(7) Exit

Your selection: """

welcome = "Welcome to your watchlist"

print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Relase date (dd-mm-yyyy): ")
    #parse the string into a datetime object(release_date string, format string(what format the string is in))
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")#object
    timestamp = parsed_date.timestamp()
    
    database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading} Movies --")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)#datetime object
        human_date = movie_date.strftime("%b %d %Y")#movie date
        print(f"{_id}: {title} (on {human_date})")# 0 = title, 1 = timestamp
    print("------\n")



def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Enter movie title you've watched: ")
    database.watched_movie(username, movie_id)

def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list("Watched", movies)
    else:
        print("That user has watched no movies yet!")


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)

while(user_input := input(menu)) != "7":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    else:
        print("Invalid input, please try agian")