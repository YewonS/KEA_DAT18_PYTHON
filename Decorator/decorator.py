import datetime

def log(func):
    def wrapper(*args):
        #write to log file
        f = open('log.txt', 'a+') # a+ => append to the end of the file. also creates file if it doesn't exist
        f.write(f'{datetime.datetime.now()}, {args} = {func(*args)} \n ')
        return func(*args) # executing func
    return wrapper 

@log
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# @log
# def printer(text):
#     print(text)