# clone_github.py

""" In this exercise you should read the content of your own github account api. 
    The url for this is https://api.github.com/users/<your-username>/repos
    
    1. Get all urls for all repositories on your account. 
    Clone all these repositories to your local computer. 
    2. Change your program into being able to "ask for" a username for any github account.
    Clone all repos from this users account. 
    3. If you did not already modualize your application do it now. 
"""

import os
import subprocess
import requests

class clone_github:

    def main():
        print('Type in your username of your github account')
        username = str(input())
        print(requests.get(f'https://api.github.com/users/{username}/repos').text)

    if __name__ == '__main__':
        main()
