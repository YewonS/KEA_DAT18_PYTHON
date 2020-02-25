# mod.py


a = 'Hello world from mod.py file a variable'

l = [1, 2, 3, 4]
s = {5, 6, 7, 8}
d = {'name': 'Claus'}
t = ('name', 'Claus')

def func():
    return 'Hello from function in mod file'

class Car:
    pass

def main():
    print(func())


if __name__ == '__main__':
    main()

    # create a module -> can be called or can be imported