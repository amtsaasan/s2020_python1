
def get_yes_no(message = "") -> str:
    '''
    Returns a Yes/No response for the user
    based on the given string argument.
    '''
    response = input(message)
    while True:
        response = response.capitalize()
        response = response.strip()
        if response == "Yes" or response == "No":
            break
        else:
            response = input('Invalid Entry. Enter "Yes" or "No": ')
    return response


def check_for_duplicate(movie_list: list, movie_name: str) -> bool:
    '''
    Returns after True if movie is found in movie list
    else, returns False.
    '''
    duplicate_movie = False
    if len(movie_list) > 0:        
        new_movie = movie_name.casefold()
        for movie in movie_list:
            if new_movie == movie[0].casefold():
                duplicate_movie = True
                break
    return duplicate_movie


def greet_user() -> None:
    '''
    Greets the user to enter movie titles and genres
    '''
    message = "Enter all your favorite movies"
    print(message)


def get_movie(user_list: list) -> list:
    '''
    Request move titles and genres from the user.
    Appends the user input to the argument list provided
    Format:
    [....
    [movie name 1, movie genre 1]
    [movie name 2, movie genre 2]
    ]
    '''
    movie_list = user_list.copy()
    while True:
        name = input("\nEnter a movie title: ").capitalize()
        
        if check_for_duplicate(movie_list, name) == False:            
            category = input(f"What genre is {name}: ").capitalize()
            movie_list.append([name, category])
        else:
            print("\nThat movie has already been submitted.")

        request = "Would you like to enter another movie? "
        if get_yes_no(request) == "No":
            break

    return movie_list




if __name__ == "__main__":
    greet_user()
    master_list = [["Title", "Genre"]]
    master_list = get_movie(master_list)
    print(master_list)
