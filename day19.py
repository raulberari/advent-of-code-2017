class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def __add__(self, point):
        return Point(self._x + point.getX(), self._y + point.getY())

    def __str__(self):
        return str(self._x) + " " + str(self._y)


def isEnd(point):
    if (visitedMatrix[point.getX() + 1][point.getY()] == 0 and
        visitedMatrix[point.getX() - 1][point.getY()] == 0 and
        visitedMatrix[point.getX()][point.getY() + 1] == 0 and
            visitedMatrix[point.getX()][point.getY() - 1] == 0):
        return True

    return False

def isOut(point):
    if not (0 <= point.getX() < 250 and 0 <= point.getY() < 250):
        return True

    return False


matrixLine = [""] * 250
matrix = []
for i in range(250):
    matrix.append(matrixLine[:])

visitedLine = [0] * 250
visitedMatrix = []
solution1 = ""
steps = 0

for i in range(250):
    visitedMatrix.append(visitedLine[:])


with open("day19.txt", "r") as readFile:
    lines = readFile.readlines()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            matrix[i][j] = lines[i][j]
            if matrix[i][j] == "\n":
                matrix[i][j] = " "

            if matrix[i][j] != " ":
                visitedMatrix[i][j] = 1

    current = None

    for i in range(len(matrix[0])):
        if matrix[0][i] == "|":
            current = Point(0, i)

    direction = "down"
    while isEnd(current) is False:
        while direction == "down" and isOut(current) is False:
            if matrix[current.getX()][current.getY()].isalpha() is True:
                solution1 += matrix[current.getX()][current.getY()]
            visitedMatrix[current.getX()][current.getY()] = 0
            current = current + Point(1, 0)
            if isOut(current) is False:
                steps += 1

                if matrix[current.getX()][current.getY()] == "+":
                    if visitedMatrix[current.getX()][current.getY() - 1] == 0:
                        direction = "right"
                    elif visitedMatrix[current.getX()][current.getY() + 1] == 0:
                        direction = "left"

        while direction == "right" and isOut(current) is False:
            if matrix[current.getX()][current.getY()].isalpha() is True:
                solution1 += matrix[current.getX()][current.getY()]
            visitedMatrix[current.getX()][current.getY()] = 0
            current = current + Point(0, 1)
            if isOut(current) is False:
                steps += 1

                if matrix[current.getX()][current.getY()] == "+":
                    if visitedMatrix[current.getX() + 1][current.getY()] == 0:
                        direction = "up"
                    elif visitedMatrix[current.getX() - 1][current.getY()] == 0:
                        direction = "down"

        while direction == "up" and isOut(current) is False:
            if matrix[current.getX()][current.getY()].isalpha() is True:
                solution1 += matrix[current.getX()][current.getY()]
            visitedMatrix[current.getX()][current.getY()] = 0
            current = current + Point(-1, 0)
            if isOut(current) is False:
                steps += 1

                if matrix[current.getX()][current.getY()] == "+":
                    if visitedMatrix[current.getX()][current.getY() - 1] == 0:
                        direction = "right"
                    elif visitedMatrix[current.getX()][current.getY() + 1] == 0:
                        direction = "left"

        while direction == "left" and isOut(current) is False:
            if matrix[current.getX()][current.getY()].isalpha() is True:
                solution1 += matrix[current.getX()][current.getY()]
            visitedMatrix[current.getX()][current.getY()] = 0

            current = current + Point(0, -1)
            if isOut(current) is False:
                steps += 1

                if matrix[current.getX()][current.getY()] == "+":
                    if visitedMatrix[current.getX() + 1][current.getY()] == 0:
                        direction = "up"
                    elif visitedMatrix[current.getX() - 1][current.getY()] == 0:
                        direction = "down"

    print(solution1)
    print(steps)

