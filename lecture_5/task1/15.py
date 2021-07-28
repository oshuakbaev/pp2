import random

def random_line(text):
    lines = open(text).read().splitlines()
    return random.choice(lines)
print(random_line('/Users/olzhas/Documents/GitHub/pp2/lecture_5/task1/w3res.txt'))