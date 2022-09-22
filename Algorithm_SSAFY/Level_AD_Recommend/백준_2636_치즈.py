import sys
from collections import deque
sys.stdin = open("input.txt", "r", encoding="utf-8")
input = sys.stdin.readline

maxY, maxX = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(maxY)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def countCheese(matrix):
    count = 0
    for y in range(maxY):
        for x in range(maxX):
            if matrix[y][x] == 1:
                count += 1
    return count


def deleteEdge(matrix):
    for y in range(maxY):
        for x in range(maxX):
            if matrix[y][x] == -1:
                matrix[y][x] = 0
    return matrix


def bfs(nowCheese):
    while q:
        y, x = q.popleft()
        for i in range(4):
            nY = y + dy[i]
            nX = x + dx[i]
            if 0 <= nY < maxY and 0 <= nX < maxX and visited[nY][nX] == 0:
                visited[nY][nX] = 1

                if matrix[nY][nX] == 1:
                    matrix[nY][nX] = -1
                    nowCheese -= 1
                else:
                    q.append((nY, nX))
    return nowCheese


totalCheese = countCheese(matrix)
time = 0
temp = totalCheese
q = deque()
while totalCheese > 0:
    visited = [[0] * maxX for _ in range(maxY)]
    q.append((0, 0))
    totalCheese = bfs(totalCheese)
    if totalCheese != 0:
        temp = totalCheese

    time += 1
    matrix = deleteEdge(matrix)

print(time)
print(temp)
