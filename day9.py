import re

with open("day9.txt", "r") as readfile:
    stream = readfile.read()

    stream = re.sub(r'!.', '', stream)

    charsBefore = len(stream)
    copy = stream
    numberOfSubsMade = re.subn('<.*?>', '', copy)[1]

    stream = re.sub('<.*?>', '', stream)

    charDifference = charsBefore - len(stream) - 2 * numberOfSubsMade
    
    score = 0
    currentScore = 0
    for char in stream:
        if char == "{":
            currentScore += 1

        if char == "}":
            score += currentScore
            currentScore -= 1

    print(score)
    print(charDifference)

