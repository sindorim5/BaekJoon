import sys
from collections import deque
sys.stdin = open("input.txt", "r", encoding="UTF-8")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input())))

visited = [[False for _ in range(n)] for _ in range(n)]

result = []


def bfs(y, x):
    q = deque()
    q.append([y, x])
    count = 0
    while q:
        nowY, nowX = q.popleft()
        visited[nowY][nowX] = True
        count += 1
        for i in range(4):
            nY = nowY + dy[i]
            nX = nowX + dx[i]
            if 0 <= nY < n and 0 <= nX < n:
                if matrix[nY][nX] == 1 and visited[nY][nX] == False:
                    if [nY, nX] not in q:
                        q.append([nY, nX])

    return count


for y in range(n):
    for x in range(n):
        if matrix[y][x] == 1 and visited[y][x] == False:
            temp = bfs(y, x)
            result.append(temp)

print(len(result))
result.sort()
for r in result:
    print(r)
