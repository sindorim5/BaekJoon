import sys
from collections import deque

sys.stdin = open("input.txt", "r", encoding="UTF-8")

N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(y, x):
    q = deque()
    changeList = []
    q.append((y, x))
    changeList.append((y, x))
    visited[y][x] = True
    while q:
        b, a = q.popleft()
        for i in range(4):
            nY = b + dy[i]
            nX = a + dx[i]
            if 0 <= nY < N and 0 <= nX < N and not visited[nY][nX]:
                if L <= abs(matrix[nY][nX] - matrix[b][a]) <= R:
                    visited[nY][nX] = True
                    changeList.append((nY, nX))
                    q.append((nY, nX))
    return changeList

count = 0
while True:
    flag = 0
    temp = []
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                visited[y][x] = True
                temp = bfs(y, x)
                if len(temp) > 1:
                    flag = 1
                    changeValue = 0
                    for t in temp:
                        changeValue += matrix[t[0]][t[1]]
                    changeValue = changeValue // len(temp)
                    for t in temp:
                        matrix[t[0]][t[1]] = changeValue
    if flag == 0:
        break
    count += 1

print(count)
