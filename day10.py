readFile = open("day10.txt", "r")
chars = readFile.read()

lengths = []
for char in chars:
    lengths.append(ord(char))

lengths.append(17)
lengths.append(31)
lengths.append(73)
lengths.append(47)
lengths.append(23)


def reverse(text, repeat):
    knot = list(range(256))
    pos = 0
    skip = 0
    for k in range(repeat):
        for i in text:
            temp = []
            for j in range(i):
                temp.append(knot[(pos + j) % 256])
            for j in range(i):
                knot[(pos + i - 1 - j) % 256] = temp[j]
            pos += skip + i
            skip += 1
    return knot


def generateDenseHash(sparce):
    denseHash = []

    for i in range(0, 256, 16):
        denseNumber = 0
        for j in range(i, i + 16):
            denseNumber = denseNumber ^ sparce[j]

        denseHash.append(hex(denseNumber)[2:])

    denseHashString = ""
    for i in range(16):
        if len(denseHash[i]) == 1:
            denseHashString += "0" + str(denseHash[i])
        else:
            denseHashString += str(denseHash[i])

    return denseHashString


sparce = reverse(lengths, 64)
denseHashString = generateDenseHash(sparce)

print(denseHashString)
