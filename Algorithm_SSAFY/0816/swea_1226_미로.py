import sys
from collections import deque

sys.stdin = open("0816/input_1226.txt", "r", encoding="utf-8")

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    matrix = []
    mapSize = 16
    q = deque()
    for _ in range(mapSize):
        temp = list(map(int, list(input())))
        matrix.append(temp)

    startY, startX = 0, 0

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    def startPoint(arr):
        for y in range(len(arr)):
            for x in range(len(arr)):
                if arr[y][x] == 2:
                    return (y, x)

    startY, startX = startPoint(matrix)

    flag = 0
    q.append((startY, startX))
    while q:
        y, x = q.popleft()
        # 도착지면 break
        if matrix[y][x] == 3:
            flag = 1
            break

        matrix[y][x] = -1
        # 아니라면 상하좌우 탐색 진행
        for i in range(4):
            nY = y + dy[i]
            nX = x + dx[i]
            if 0 <= nY < mapSize and 0 <= nX < mapSize:
                if matrix[nY][nX] == 0 or matrix[nY][nX] == 3:
                    q.append((nY, nX))

    print("#{} {}".format(test_case, flag))
