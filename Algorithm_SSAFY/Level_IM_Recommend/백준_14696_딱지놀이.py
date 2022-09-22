import sys

sys.stdin = open("./input.txt", "r", encoding="utf-8")

round = int(input())


def winCheck(a, b, idx):
    if a[idx] > b[idx]:
        return "A"
    elif a[idx] < b[idx]:
        return "B"
    else:
        idx -= 1
        if idx == 0:
            return "D"
        else:
            return winCheck(a, b, idx)


for r in range(round):
    aPoint = [0, 0, 0, 0, 0]
    bPoint = [0, 0, 0, 0, 0]

    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))

    for i in range(1, len(aList)):
        aPoint[aList[i]] += 1

    for i in range(1, len(bList)):
        bPoint[bList[i]] += 1

    result = winCheck(aPoint, bPoint, 4)

    print(result)
