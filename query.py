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
def cast_search(answer):
    answer = str(answer).lower()
    for i in range(len(movies._movies)):
        castFound = False
        for j in range(len(movies._movies[i]['cast'])):
            if movies._movies[i]['cast'][j].lower().__contains__(answer):
                castFound = True
        if castFound:
            print(movies._movies[i]['name'])
            print("[", end = ' ')
            for k in range(0,len(movies._movies[i]['cast'])):
                if movies._movies[i]['cast'][k].lower().__contains__(answer):
                    print(movies._movies[i]['cast'][k], end = ' ')
            print("]")
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