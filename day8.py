variables = [0] * 19000
maxList = []


def valueOfString(chars):
    val = 0
    for char in chars:
        val = val * 26 + (ord(char) - ord('a') + 1)

    return val

with open("day8.txt", 'r') as readFile:
    lines = readFile.readlines()

    for line in lines:
        words = line.split()

        register2 = variables[valueOfString(words[4])]

        if ((words[5] == ">" and register2 > int(words[6])) or
            (words[5] == ">=" and register2 >= int(words[6])) or
            (words[5] == "==" and register2 == int(words[6])) or
            (words[5] == "!=" and register2 != int(words[6])) or
            (words[5] == "<=" and register2 <= int(words[6])) or
                (words[5] == "<" and register2 < int(words[6]))):

            if words[1] == "inc":
                variables[valueOfString(words[0])] += int(words[2])
            elif words[1] == "dec":
                variables[valueOfString(words[0])] -= int(words[2])

        maxList.append(max(variables))

print(max(variables))
print(max(maxList))

