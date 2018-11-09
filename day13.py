import re
import datetime

indexes = [0] * 100
direction = ["down"] * 100
walls = [0] * 100
numberOfWalls = 0
half = "second"
wallsCopy = []
indexesCopy = []


def moveIndex(start):
    for i in range(start, len(walls)):
        if walls[i] != 0:
            if indexes[i] == walls[i]:
                direction[i] = "up"
            elif indexes[i] == 1:
                direction[i] = "down"

            if direction[i] == "down":
                indexes[i] += 1
            elif direction[i] == "up":
                indexes[i] -= 1



def getScore(walls2, indexes2):
    score = 0

    wallsC = walls2[:]
    indexesC = indexes2[:]

    for i in range(numberOfWalls + 1):
        if indexesC[i] == 1:
            score += i * wallsC[i]
        moveIndex(0)

    return score


with open("day13.txt", "r") as readFile:
    lines = readFile.readlines()
    for line in lines:
        line = re.sub(r'[\n:]', '', line)
        args = line.split(' ')
        walls[int(args[0])] = int(args[1])
        indexes[int(args[0])] = 1
        wallsCopy = walls[:]
        indexesCopy = indexes[:]
        numberOfWalls = int(args[0])

    if half == "first":
        print(getScore(walls, indexes))

    elif half == "second":

        for i in range(numberOfWalls):
            moveIndex(i + 1)
        # indexes = moveIndex(walls, indexes, 1)
        # indexes = moveIndex(walls, indexes, 2)
        # indexes = moveIndex(walls, indexes, 3)
        # indexes = moveIndex(walls, indexes, 4)
        # indexes = moveIndex(walls, indexes, 5)
        # indexes = moveIndex(walls, indexes, 6)

        for i in range(10000000):

            # t1 = datetime.datetime.now()
            moveIndex(0)
            if 1 not in indexes:
                print(indexes)
                print(i + 1)
                break

            # print(datetime.datetime.now() - t1)
        # indexes[1:] = moveIndex(walls, indexes[1:], 1)
        # print(indexes)

