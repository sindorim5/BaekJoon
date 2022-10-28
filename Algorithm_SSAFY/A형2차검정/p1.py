import sys

# sys.stdin = open("input.txt", "r", encoding="UTF-8")
sys.stdin = open("sampleinput1.txt", "r", encoding="UTF-8")


T = int(input())


def checkDay(number):
    day = 1
    water = 0
    while number >= 0:
        if day % 2 == 1:
            water = 1
        elif day % 2 == 0:
            water = 2

        if number == 2:
            if water == 2:
                return day
            elif water == 1:
                return day + 1
        elif number - water > 0:
            number -= water
            day += 1
        elif number - water == 0:
            return day
        elif number - water < 0:
            day += 1


for test_case in range(1, T + 1):
    n = int(input())
    treeList = list(map(int, input().split()))
    maxTreeHeight = max(treeList)

    for i in range(len(treeList)):
        if treeList[i] <= maxTreeHeight:
            treeList[i] = maxTreeHeight - treeList[i]

    sumHeight = sum(treeList)

    if sumHeight == 0:
        print("#{} {}".format(test_case, 0))
        continue

    minDay = checkDay(sumHeight)

    print("#{} {}".format(test_case, minDay))