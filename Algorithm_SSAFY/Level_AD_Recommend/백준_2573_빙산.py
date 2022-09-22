import sys
from collections import deque

sys.stdin = open("input.txt", "r", encoding="utf-8")
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
time = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = True
    seaList = []

    while q:
        y, x = q.popleft()
        sea = 0
        for i in range(4):
            nY = y + dy[i]
            nX = x + dx[i]
            if 0 <= nY < n and 0 <= nX < m:
                if not matrix[nY][nX]:
                    sea += 1
                elif matrix[nY][nX] and visited[nY][nX] == False:
                    q.append((nY, nX))
                    visited[nY][nX] = True
        if sea > 0:
            seaList.append((y, x, sea))
    for y, x, sea in seaList:
        matrix[y][x] = max(0, matrix[y][x] - sea)

    return 1


ice = []
for y in range(n):
    for x in range(m):
        if matrix[y][x]:
            ice.append((y, x))
while ice:
    visited = [[False] * m for _ in range(n)]
    delList = []
    count = 0
    for y, x in ice:
        if matrix[y][x] and visited[y][x] == False:
            count += bfs(y, x)
        if matrix[y][x] == 0:
            delList.append((y, x))
    if count > 1:
        print(time)
        break
    ice = sorted(list(set(ice) - set(delList)))
    time += 1

if count < 2:
    print(0)
