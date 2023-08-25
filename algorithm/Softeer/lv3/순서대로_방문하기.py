import sys


def dfs(points, depth):
    if (depth == m):
        result.append(points)
        return

    if (points[-1] == checkPoints[depth]):
        dfs(points, depth + 1)
        return

    for i in range(4):
        nY = points[-1][0] + dY[i]
        nX = points[-1][1] + dX[i]

        if (nY < 0 or nX < 0 or nY >= n or nX >= n):
            continue

        if (matrix[nY][nX] == 1):
            continue

        if [nY, nX] not in points:
            dfs(points + [[nY, nX]], depth)


dY = [1, 0, -1, 0]
dX = [0, 1, 0, -1]

n, m = map(int, input().split())
matrix = []
checkPoints = []
result = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(m):
    y, x = map(int, input().split())
    checkPoints.append([y-1, x-1])

dfs([checkPoints[0]], 0)

print(len(result))
