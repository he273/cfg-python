clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]

if clothes[0] == "shorts":
    clothes[0] = "warm coat"
    print(clothes)
else:
    print(clothes)

scores = [150, 320, 120, 540, 230, 760, 430, 840, 250, 650]
print(len(scores))
print(max(scores))
print(min(scores))

print(sorted(scores))
sorted_scores = sorted(scores)
print(list(reversed(sorted_scores)))

shopping_list = [
    'bread',
    'cheese',
    'pop tarts',
    'carrots',
]

if 'bread' in shopping_list:
    shopping_list.append('butter')

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0

for student_name in student_names:
    if student_name.startswith('H'):
        count = count + 1

print(count)

import random

first_names = ['ben', 'fran', 'rachel', 'john', 'bryan']
last_names = ['smith', 'brown', 'thompson', 'james']

print('Random name is {} {}'.format(random.choice(first_names), random.choice(last_names)))