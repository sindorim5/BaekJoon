import sys
from collections import deque
sys.stdin = open("1006/input.txt", "r", encoding="UTF-8")

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    matrix = []
    devilMatrix = [[-1 for _ in range(m)] for _ in range(n)]
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    start, dest, devil = [], [], []

    for y in range(n):
        temp = list(input())
        for x in range(m):
            if (temp[x] == "S"):
                start = [y, x]
            elif (temp[x] == "D"):
                dest = [y, x]
            elif (temp[x] == "*"):
                devil = [y, x]
        matrix.append(temp)

    # 악마 depth 찍기
    q = deque()
    y, x = devil[0], devil[1]
    depth = 0
    q.append([y, x, depth])
    while q:
        y, x, depth = q.popleft()
        devilMatrix[y][x] = depth
        for i in range(4):
            nY = y + dy[i]
            nX = x + dx[i]
            if 0 <= nY < n and 0 <= nX < m:
                if matrix[nY][nX] != ".":
                    continue
                if devilMatrix[nY][nX] == -1:
                    q.append([nY, nX, depth + 1])

    # 수연 출발
    q = deque()
    y, x = start[0], start[1]
    endY, endX = dest[0], dest[1]
    depth = 0
    flag = 0
    q.append([y, x, depth])
    while q:
        y, x, depth = q.popleft()
        visited[y][x] = depth
        if y == endY and x == endX:
            flag = 1
            break
        for i in range(4):
            nY = y + dy[i]
            nX = x + dx[i]
            if 0 <= nY < n and 0 <= nX < m:
                if visited[nY][nX] != -1:
                    continue
                if devilMatrix[nY][nX] >= depth:
                    continue
                if matrix[nY][nX] == "X" or matrix[nY][nX] == "S":
                    continue
                q.append([nY, nX, depth + 1])

    if flag == 1:
        print("#{} {}".format(test_case, depth))
    else:
        print("#{} GAME OVER".format(test_case))
