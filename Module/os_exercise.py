# os_exercise.py
# Do the following task using the os module

"""
1. create a folder and name the folder 'os_exercises.'                                                  
2. In that folder create a file. Name the file 'exercise.py'                                                                            
3. get input from the console and write it to the file.                                                 
4. repeat step 2 and 3 (name the file something else).                                                  
5. read the content of the files and and print to console the content of the file with the largest amount of unique words.
"""

import os

# 5

def unique_words(thefile):
    t = set(thefile.read().split())
    return t


#1

if os.path.isdir('os_exercises'):
    pass
else:
    os.mkdir('os_exercises')

os.chdir('os_exercises')


#2 - 5 

for i in range(1, 4):
    if os.path.exists(f'exercise{i}.py'):
        print(unique_words(open(f'exercise{i}.py')))
    else:
        newFile = open(f'exercise{i}.py', 'w')
        newInput = str(input())
        newFile.write(newInput)
        print(f'new File created: "{newFile}", {newInput}')
        newFile.close()
