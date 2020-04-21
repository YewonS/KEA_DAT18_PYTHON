import random

# School of students
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def students_list(num_students):
    newList = []
    for i in range(num_students):
        people = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        newList.append(people)
    return newList

def students_generator(num_students):
    for i in xrange(num_students):
        people = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield people

people = students_list(1000000)
people = students_generator(1000000)

