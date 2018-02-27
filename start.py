import sys
from auth import *
from game.game import init_game
from blog.blog import init_blog
from bible.bible import init_bible
from ninja.ninja import init_ninja

def init_menu(option = 0) :
    if option < 1 :
        print("~~ S T A R T ~~ \n \n[1] Play a game \n[2] Update Blog\n[3] My Bible \n[4] Ninja Py \n")

        option = int(input("Select an option >"))
        
    if option == 1 :
        init_game(username)
        init_menu()
    elif option == 2 :
        init_blog(username)
    elif option == 3 :
        init_bible(username)
    elif option == 4 :
        init_ninja(username)
        init_menu()
    else :
        print("Not an option \n")
        init_menu()

print("Welcome...")

username = ""
password = ""
menu = []

if len(sys.argv) <= 1 :
    username = ""
elif len(sys.argv) == 2 :
    username = sys.argv[1]
elif len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]
else :
    username = sys.argv[1]
    password = sys.argv[2]
    menu = (sys.argv[3]).split("=")


auth = False
if username == "":
    is_new = ""
    while is_new != "Y" :
        is_new = input("Is this your first time? (Y/N) >")

        if is_new == "Y" or is_new == "y" :
            user_exist = False
            while user_exist == False:
                username = input("Enter a username >")
                user_exist = check_user(username)
                if user_exist == True :
                    print("Hello, " + username)
                    password = input("Enter a password >")
                    
                    auth = signup(username, password)
                    
                    if auth == True :
                        init_menu()

        elif is_new == "N" or is_new == "n" :
            while auth == False:
                username = input("Enter your username >")
                password = input("Enter your password, " + username + " >")

                auth = login(username, password)
                
                if auth == True :
                    init_menu()

        else:
            print("Not an option")

elif len(username) > 1 and len(password) > 1 :
    auth = login(username, password)

    if auth == True :
        print("Hello, " + username + "\n")
        if len(menu) > 1 :
            init_menu(int(menu[1]))
        else:
            init_menu()


else:
    print("Hello " + username)
    if password == "" :
        while auth == False :
            password = input("Enter your password >")

            auth = login(username, password)

            if auth == True :
                init_menu()
