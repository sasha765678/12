import random

for i in range(random.randint(30, 50)):
    for j in range(random.randint(30, 50)):
        print(random.choice(('#', '#', '#', '.', '.', '.', '$', '-')), end='')
    print()
