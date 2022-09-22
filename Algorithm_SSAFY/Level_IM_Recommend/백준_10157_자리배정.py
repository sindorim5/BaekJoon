import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

c, r = map(int, input().split())
target = int(input())

if target > c * r:
    print(0)
    exit()

matrix = [[0] * c for _ in range(r)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

num = 1
idx = 0

y = 0
x = 0
while True:
    if num == target:
        print(x + 1, y + 1)
        break

    matrix[y][x] = num
    nY = y + dy[idx]
    nX = x + dx[idx]

    if nY < 0 or nY >= r or nX < 0 or nX >= c or matrix[nY][nX] != 0:
        idx = (idx + 1) % 4
        nY = y + dy[idx]
        nX = x + dx[idx]
    y = nY
    x = nX
    num += 1
