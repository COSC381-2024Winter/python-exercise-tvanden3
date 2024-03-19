from movies import Movies

movies = Movies('./movies.txt')
def movies_n(answer):
    for i in range(len(movies._movies)):
        if str(answer).lower() in movies._movies[i]['name'].lower():
            print(movies._movies[i]['name'])
    print()   
def movie_list():
    for i in range(len(movies._movies)):
        print(movies._movies[i]['name'])
    print()
#def cast_search(answer)
choice = ' '


while choice != 'q':
    print("sn: Search Movies by Name")
    print("sc: Search by Cast")
    print("list: Print all the Movie Names")
    print("q: quit") 
    choice = input("").lower()
    print()

    if choice == "sn":
        keyb = input("enter a word to search: ")
        movies_n(keyb)

    elif choice == "list":
       movie_list()
    
    elif choice == "sc":
        keyb = input("enter a word to search: ")
        cast_search(keyb)