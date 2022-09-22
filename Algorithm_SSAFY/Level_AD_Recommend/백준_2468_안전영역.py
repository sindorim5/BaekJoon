import sys
from collections import deque

sys.stdin = open("input.txt", "r", encoding="utf-8")
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
maxHeight = max(map(max, matrix))
maxCount = 0

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(b, a, rain):
    q = deque()
    q.append((b, a))
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for i in range(4):
            nY = y + dy[i]
            nX = x + dx[i]
            if (
                0 <= nY < n
                and 0 <= nX < n
                and matrix[nY][nX] > rain
                and visited[nY][nX] == False
            ):
                if (nY, nX) not in q:
                    q.append((nY, nX))


for rain in range(maxHeight):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for y in range(n):
        for x in range(n):
            if matrix[y][x] > rain and visited[y][x] == False:
                bfs(y, x, rain)
                count += 1

    if maxCount < count:
        maxCount = count

print(maxCount)
