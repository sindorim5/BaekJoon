import sys
from collections import deque
sys.stdin = open("./0913/보급로.txt", "r", encoding="UTF-8")

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    q = deque()
    q.append([y, x, 0])
    visited[y][x] = 0
    while q:
        nowY, nowX, value = q.popleft()
        for i in range(4):
            nY = nowY + dy[i]
            nX = nowX + dx[i]
            if 0 <= nY < n and 0 <= nX < n:
                nextValue = matrix[nY][nX]
                if visited[nY][nX] > value + nextValue:
                    visited[nY][nX] = value + nextValue
                    q.append([nY, nX, value + nextValue])


for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    visited = [[999999999] * n for _ in range(n)]
    visited[0][0] = 0
    bfs(0, 0)
    print("#{} {}".format(test_case, visited[n-1][n-1]))
