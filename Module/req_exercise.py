# Create an application that asks for an url. 
# Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. Locally means that you should be able to cut your internet connection and still have a functionig html page. 
# when done push all files to you github account. (you are allowed to manualy create an online repo and feed the clone url to your program. but the rest should be done through python).

# You will have to use the requests module, the OS module and the subprocesses module for this taks. 

import os, requests, subprocess

print("Type in the name of the webpage: ")
url = input()

if os.path.exists(f'{url}.html'):
    print("The page is already downloaded.")
else:   
    r = requests.get(f'https://www.{url}.com')
    r = r.text
    newFile = open(f'{url}.html', 'w+')
    newFile.write(r)
    print('operation succeed. you can go home now')



