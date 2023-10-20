import random
die = 0

while True:
    list = ["yes", "no", "y", "n", "YES", "NO", "Y", "N"]
    thing = random.choice(list)
    prompt = input("Type {}>>> ".format(thing))
    if prompt == thing:
        break
    else:
        die += 1
    if die >= 3:
        break
