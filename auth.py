def login(username, password) :
    user_data = username + ":" + password + "\n"
    try:
        auth_data = open("start.auth", "r")
    except FileNotFoundError :
        print("Wrong Username or Password \n")
        return False
    
    auth_state = False
    # print auth_data.readlines()
    for auth in auth_data :
        if user_data == auth :
            print("Signed in")
            auth_state = True
            return auth_state
    if auth_state != True :
        print("Wrong Username or Password \n")
        return False
    auth_data.close()
    

def signup(username, password) :
    user_data = [username + ":" + password, '\n']
    auth_data = open("start.auth", "a")
    auth_data.writelines(user_data)
    print("\nRegistration complete \n \nYou can START next by placing your username and password as arguement \ne.g $ python start.py [username] [password] \noptional parameter menu=[option]\n")
    auth_data.close()
    return True
    
def check_user(username) :
    try:
        auth_data = open("start.auth", "r")
    except FileNotFoundError :
        return True

    auth_state = False

    for auth in auth_data :
        auth = auth.replace("\n", "").split(":")
        if auth[0] == username :
            print("username already exist \n")
            auth_state = False
            break
        else :
            auth_state = True

    if auth_state == False :
        return False
    else:
        return True
        
