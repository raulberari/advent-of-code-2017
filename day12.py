def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    for next in set(graph[start]) - visited:
        dfs(graph, next, visited)

    return visited


with open("day12.txt", "r") as readFile:
    graph = {}

    lines = readFile.readlines()

    for line in lines:
        args = line.split()
        args = [arg.strip(',') for arg in args]
        vertices = [int(arg) for arg in args[2:]]

        graph[int(args[0])] = vertices

    listOfSets = []

    for i in range(len(graph)):
        connectedPart = dfs(graph, i)

        if connectedPart not in listOfSets:
            listOfSets.append(connectedPart)

    print(len(dfs(graph, 0)))  # 1st part
    print(len(listOfSets))  # 2nd part
