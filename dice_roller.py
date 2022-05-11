import random as r


def dice_roller():
    n = ''
    while not n.strip().isdigit() or int(n.strip()) < 1:
        n = input("Enter the number of sides on your die: ")

    x = r.randrange(1, int(n))
    print("You rolled a {} on an {} sided die.".format(x, n))


dice_roller()
