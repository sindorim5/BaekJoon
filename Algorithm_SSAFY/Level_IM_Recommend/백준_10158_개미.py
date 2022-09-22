import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

maxX, maxY = map(int, input().split())
x, y = map(int, input().split())
target = int(input())

xList = list(range(maxX))
for i in range(maxX, 0, -1):
    xList.append(i)

yList = list(range(maxY))
for j in range(maxY, 0, -1):
    yList.append(j)

x += target
y += target

x = xList[x % len(xList)]
y = yList[y % len(yList)]

print(x, y)
