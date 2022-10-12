import sys

from collections import deque
sys.stdin = open("input.txt", "r", encoding="UTF-8")
n, m = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

matrix = [list(input()) for _ in range(n)]

def bfs(y, x):
    global maxValue
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((y, x, 0))
    while q:
        nowY, nowX, depth = q.popleft()
        visited[nowY][nowX] = True
        maxValue = max(maxValue, depth)
        for i in range(4):
            nY = nowY + dy[i]
            nX = nowX + dx[i]
            if 0 <= nY < n and 0 <= nX < m:
                if matrix[nY][nX] == "L" and visited[nY][nX] == False:
                    if (nY, nX, depth+1) not in q:
                        q.append((nY, nX, depth+1))

maxValue = -999999999
for y in range(n):
    for x in range(m):
        if matrix[y][x] == "L":
            num = 0
            for i in range(4):
                nY = y + dy[i]
                nX = x + dx[i]
                if 0 <= nY < n and 0 <= nX < m and matrix[nY][nX] == "L":
                    num += 1
            if 0 < num <= 2:
                bfs(y, x)


print(maxValue)
