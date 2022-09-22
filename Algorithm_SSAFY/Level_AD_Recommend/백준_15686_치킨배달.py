import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
houseList = []
chickenList = []
minValue = 999999999

for y in range(n):
    for x in range(n):
        if matrix[y][x] == 1:
            houseList.append((y, x))
        if matrix[y][x] == 2:
            chickenList.append((y, x))


def pickM():
    result = []

    def picking(idx, nowPick):
        if len(nowPick) == m:
            result.append(nowPick)
            return
        for i in range(idx, len(chickenList)):
            picking(i + 1, nowPick + [chickenList[i]])

    picking(0, [])

    return result


pickList = pickM()

for pick in pickList:
    sumValue = 0
    for house in houseList:
        houseMin = 999999999
        for p in pick:
            hY, hX = house
            pY, pX = p
            temp = abs(hY - pY) + abs(hX - pX)
            if houseMin > temp:
                houseMin = temp
        sumValue += houseMin
    if minValue > sumValue:
        minValue = sumValue

print(minValue)
