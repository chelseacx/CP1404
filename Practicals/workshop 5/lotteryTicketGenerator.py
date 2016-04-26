
import random

numberOfQuickPicks = int(input("How many quick picks? "))

for x in range(numberOfQuickPicks):
    quickPickLine = []
    while len(quickPickLine) != 6:
        randomNumber = random.randint(1, 45)
        if randomNumber not in quickPickLine:
            quickPickLine.append(randomNumber)
    quickPickLine.sort()

    n = 0
    line = ""
    while n != 6:

        line += "{:>2d} ".format(quickPickLine[n])
        n += 1
    print(line)

