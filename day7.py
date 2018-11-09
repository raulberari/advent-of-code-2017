class Node(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        ret = "\t" * level + self.name + " " + str(self.weight) + " " + str(self.getTotalWeight()) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)

        # childrenWeights = [child.getTotalWeight() for child in self.children]
        # ret += str(len(set(childrenWeights)))
        return ret

    def getHeight(self):
        if len(self.children) == 0:
            return 1
        else:
            maxHeight = -1
            for child in self.children:
                height = child.getHeight()
                if height > maxHeight:
                    maxHeight = height

            return 1 + maxHeight

    def getTotalWeight(self):
        if len(self.children) == 0:
            return self.weight
        else:
            totalWeight = self.weight
            for child in self.children:
                totalWeight += child.getTotalWeight()

            return totalWeight

    def isUnbalancedNode(self):
        if len(self.children) == 0:
            return False
        else:
            childrenWeights = [child.getTotalWeight() for child in self.children]
            if len(set(childrenWeights)) == 1:
                return False
            return True

nodeList = []

with open("day7.txt", "r") as readFile:
    lines = readFile.readlines()

    for line in lines:
        words = line.split()
        words[1] = words[1].strip("()")

        node = Node(words[0], int(words[1]))
        nodeList.append(node)

    for line in lines:
        words = line.split()
        if len(words) > 2:
            children = words[3:]
            children = [child.strip(',') for child in children]

            for child in children:
                for node in nodeList:
                    if node.name == child:
                        nodeList[lines.index(line)].addChild(node)


# print(nodeList[357])
maxHeights = [node.getHeight() for node in nodeList]

for node in nodeList:
    if node.isUnbalancedNode() is True:
        print(node)
