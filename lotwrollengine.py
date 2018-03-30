import random

def roll(dice):
    rolled = {}
    for i in range(dice):
        roll = random.randint(0,9)
        rolled[roll] = rolled.setdefault(roll, 0) + 1
    sorting = []
    for i in iter(rolled):
        sorting.append((rolled[i]*10)+i)
    sorting.sort(reverse=True)
    returner = []
    for i in enumerate(sorting):
        returner.append("Set #{}: {}".format(i[0]+1, i[1]))
    return returner
