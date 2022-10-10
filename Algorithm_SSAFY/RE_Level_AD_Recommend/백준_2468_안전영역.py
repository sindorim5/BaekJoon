from collections import deque
import sys

sys.stdin = open("input.txt", "r", encoding="UTF-8")


n = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

matrix = [list(map(int, input().split())) for _ in range(n)]

maxRain = max(map(max, matrix))
maxArea = 0


def bfs(y, x, rain, visited):
    q = deque()
    q.append((y, x))
    while q:
        nowY, nowX = q.popleft()
        visited[nowY][nowX] = True
        for i in range(4):
            nY = nowY + dy[i]
            nX = nowX + dx[i]
            if 0 <= nY < n and 0 <= nX < n:
                if matrix[nY][nX] > rain and visited[nY][nX] == False:
                    if (nY, nX) not in q:
                        q.append((nY, nX))


for rain in range(maxRain):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for y in range(n):
        for x in range(n):
            if matrix[y][x] > rain and visited[y][x] == False:
                count += 1
                bfs(y, x, rain, visited)

    maxArea = max(count, maxArea)

print(maxArea)
