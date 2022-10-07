import sys
from collections import deque
sys.stdin = open("input.txt", "r", encoding="UTF-8")

r, c = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

matrix = []
beaver, hedgehog, water = [], [], []

for y in range(r):
    temp = list(input())
    for x in range(c):
        if temp[x] == "D":
            beaver = [y, x]
        elif temp[x] == "S":
            hedgehog = [y, x]
        elif temp[x] == "*":
            water.append([y, x])
    matrix.append(temp)

waterQ = deque()

for w in water:
    waterQ.append(w)

hedgehogQ = deque([hedgehog + [0]])
flag = 0
while True:
    waterNextQ = deque()
    hedgehogNextQ = deque()

    while waterQ:
        y, x = waterQ.popleft()
        for i in range(4):
            nY = y + dy[i]
            nX = x + dx[i]
            if 0 <= nY < r and 0 <= nX < c:
                if matrix[nY][nX] == "D":
                    continue
                if matrix[nY][nX] == "X":
                    continue
                if matrix[nY][nX] == "." or matrix[nY][nX] == "S":
                    matrix[nY][nX] = "*"
                    if [nY, nX] not in waterNextQ:
                        waterNextQ.append([nY, nX])

    while hedgehogQ:
        y, x, depth = hedgehogQ.popleft()
        if matrix[y][x] == "D":
            flag = 1
            break
        for i in range(4):
            nY = y + dy[i]
            nX = x + dx[i]
            if 0 <= nY < r and 0 <= nX < c:
                if matrix[nY][nX] == "*":
                    continue
                if matrix[nY][nX] == "X":
                    continue
                if [nY, nX, depth+1] not in hedgehogNextQ:
                    hedgehogNextQ.append([nY, nX, depth+1])

    if flag == 1:
        print(depth)
        exit()

    if len(hedgehogNextQ) == 0:
        print("KAKTUS")
        exit()
    else:
        hedgehogQ = hedgehogNextQ.copy()
        waterQ = waterNextQ.copy()
