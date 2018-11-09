spinLock = [0]
numberOfSteps = 355

index = 0
value = 1
length = 1
for i in range(50000000):
    index += numberOfSteps
    index %= length
    index += 1
    if index == 1:
        spinLock.insert(index, i + 1)

    # print(spinLock)
    length += 1
print(spinLock)

