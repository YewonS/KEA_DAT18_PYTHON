# Exercise:
#	* Create a login application, that can store and handle multiple users.
#	* The user should be asked if he wants to log in or create a login.
#	* If 'create': The users credentials should be written to a file
#	* If 'login': The users information should be checked agains the content of the file. 
#	* The user should be granted or denied acces. 
#
# Go for the simplest, easiest, fastest approach!
#
# Most of what you need we already have covered, the rest is easy.
# You get 15 min. 
# Then we do it together

import json

def createAccount():
    print("Type in your user name: ")
    username = str(input())
    print("Type in your password: ")
    password = str(input())

    user = {f'{username}' : password}
    with open('users.txt', 'w') as theFile:
        theFile.write(json.dumps(user))


def login():    
    print("Username: ")
    user = input()
    print("Password: ")
    passw = input()

    with open('users.txt', 'r') as theFile:
        fileData = json.loads(theFile.read())
        for data in fileData:
            if (user in fileData.keys()) and (passw in fileData.values()):
                print ("Login successful!")
                return True
            else:
                print ("Wrong username/password")
                return False

def main():
    print('Type 1 to create account. Type 2 to log in.')
    newinput = int(input())
    if newinput == 1:
        createAccount()
    elif newinput == 2:
        login()
    else:
        print('Nope. Wrong input.')
    

main()