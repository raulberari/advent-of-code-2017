from operator import add

position = [0, 0, 0]
maxDistance = 0

with open("day11.txt", "r") as readFile:
    line = readFile.read().strip("\n")
    args = line.split(",")

    for arg in args:
        if arg == "nw":
            position = [sum(x) for x in zip(position, [-1, 1, 0])]

        elif arg == "n":
            position = [sum(x) for x in zip(position, [0, 1, -1])]

        elif arg == "ne":
            position = [sum(x) for x in zip(position, [1, 0, -1])]

        elif arg == "se":
            position = [sum(x) for x in zip(position, [1, -1, 0])]

        elif arg == "s":
            position = [sum(x) for x in zip(position, [0, -1, 1])]

        elif arg == "sw":
            position = [sum(x) for x in zip(position, [-1, 0, 1])]

        distance = (abs(position[0]) + abs(position[1]) + abs(position[2])) / 2
        if distance > maxDistance:
            maxDistance = distance

    print(position)
    distance = (abs(position[0]) + abs(position[1]) + abs(position[2])) / 2
    print(distance)
    print(maxDistance)
