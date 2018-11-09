banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

banksHistory = []
steps = 0

while banks not in banksHistory:
    banksHistory.append(banks[:])

    maximum = max(banks)
    maxIndex = banks.index(maximum)

    banks[maxIndex] = 0
    while maximum > 0:
        if maxIndex + 1 < len(banks):
            maxIndex += 1
        else:
            maxIndex -= len(banks) - 1

        banks[maxIndex] += 1
        maximum -= 1

    # print(banks)
    steps += 1

print(steps)
print(len(banksHistory) - banksHistory.index(banks))


