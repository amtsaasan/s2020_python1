import sys
import os

genres = {}
genres_list_count = []

def find_file() -> list:
    global movie_list
    user_input = input("Enter the path of your file: ")
    assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
    f = open(user_input,'r+')
    movie_list = [line.strip() for line in f]
    print (movie_list)
    return movie_list
    f.close()   

def sort():
    counter = 1
    for each in movie_list:
        currentline = each.split(", ")
        movie_genre = str(currentline[counter])
        if currentline[counter] not in genres:
            genres[movie_genre] = 1
        elif currentline[counter] in genres:
            genres[movie_genre] = genres[movie_genre] + 1
            
def dict_to_list():
    global genres
    global genres_list_count
    for element in genres:
        print(element)
        genres_list_count.append([element, element.value()])
            

if __name__ == "__main__":
    find_file()
    sort()
    dict_to_list()
    print(genres_list_count)
    
    print("Happy birtday")
    
