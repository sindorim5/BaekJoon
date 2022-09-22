import sys
from collections import deque

sys.stdin = open("./0915/행렬찾기.txt", "r", encoding="UTF-8")

T = int(input())

# 하, 우
dy = [1, 0]
dx = [0, 1]


def bfs(y, x):
    global points
    temp = [[y, x]]
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        nowY, nowX = q.popleft()
        for i in range(2):
            nY = nowY + dy[i]
            nX = nowX + dx[i]
            if 0 <= nY < n and 0 <= nX < n and not visited[nY][nX] and matrix[nY][nX] > 0:
                visited[nY][nX] = True
                q.append((nY, nX))
                temp.append([nY, nX])
    points.append([temp[0], temp[-1]])


for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    points = []
    result = []
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and matrix[y][x] > 0:
                bfs(y, x)

    for point in points:
        diffY = abs(point[0][0] - point[1][0]) + 1
        diffX = abs(point[0][1] - point[1][1]) + 1
        area = diffY * diffX
        result.append([area, diffY, diffX])

    result.sort()

    print("#{} {}".format(test_case, len(result)), end=" ")
    for element in result:
        print("{} {}".format(element[1], element[2]), end=" ")
    print()
