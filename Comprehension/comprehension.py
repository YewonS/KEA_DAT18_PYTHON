import string

# normal solution
a = list(string.ascii_uppercase)
# comprehension solution
a = [chr(i) for i in range(65, 91)]

# normal if
l = []
for i in range(1, 10):
    if i % 2 == 0:
        l.append(i)

# comprehension if
l = [i for i in range(1, 10) if i % 2 == 0]

# comprehension if/else
l1 = [i if i % 2 == 0 else "un-even" for i in range(1, 10)]

# comprehension nested for loop
l3 = [(i, j) for i in range(5) for j in range(i)]


# exercises
alphabets = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]]

f = ord('f')
o = ord('o')
a = ord('a')
z = ord('z')
alphabets1 = [chr(i) for i in range(a, z) if i not in range(f, o, 2)]

l2 = [i if (i % 2 == 0) else 'un-even and small' if i < 5 else 'un-even and large' for i in range(1, 10)]

colors = ['Black', 'White']
sizes = ['xs', 's', 'm', 'l', 'xl']
sold_out = [('Black', 'm'), ('White', 's')]
l4 = [(i, j) for i in colors for j in sizes if (i, j) not in sold_out]


colors = {'♠', '♡', '♢', '♣'}
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
dict1 = {color:numbers for color in colors}
