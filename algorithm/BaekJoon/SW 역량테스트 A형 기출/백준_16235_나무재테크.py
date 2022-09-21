import sys

sys.stdin = open("input.txt", "r", encoding="UTF-8")

n, m, k = map(int, input().split())

# 8방향
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]


aList = [list(map(int, input().split())) for _ in range(n)]
food = [[5 for _ in range(n)] for _ in range(n)]
matrix = [[[] for _ in range(n)]for _ in range(n)]

for i in range(m):
    y, x, age = map(int, input().split())
    matrix[y-1][x-1].append(age)

year = 0
while year < k:
    # spring
    waiting = []
    for y in range(n):
        for x in range(n):
            if matrix[y][x]:
                trees = matrix[y][x]
                trees.sort()
                removeIdx = []
                for i in range(len(trees)):
                    if food[y][x] - trees[i] >= 0:
                        food[y][x] -= trees[i]
                        trees[i] += 1
                    else:
                        waiting.append([y, x, trees[i] // 2])
                        removeIdx.append(i)
                for i in range(len(removeIdx)):
                    trees.pop(-1)
    # summer
    for wait in waiting:
        y, x, f = wait
        food[y][x] += f
    # autumn and winter
    for y in range(n):
        for x in range(n):
            food[y][x] += aList[y][x]
            if matrix[y][x]:
                trees = matrix[y][x]
                for i in range(len(trees)):
                    if trees[i] % 5 == 0:
                        for d in range(8):
                            nY = y + dy[d]
                            nX = x + dx[d]
                            if 0 <= nY < n and 0 <= nX < n:
                                matrix[nY][nX].append(1)
    year += 1

result = 0
for y in range(n):
    for x in range(n):
        if matrix[y][x]:
            result += len(matrix[y][x])

print(result)
