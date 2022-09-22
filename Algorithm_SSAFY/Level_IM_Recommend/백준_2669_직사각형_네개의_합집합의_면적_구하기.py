import sys

sys.stdin = open("./input.txt", "r", encoding="utf-8")

square = [list(map(int, input().split())) for _ in range(4)]
matrix = [[0] * 100 for _ in range(100)]
result = 0

for i in range(len(square)):
    x1, y1, x2, y2 = square[i][0], square[i][1], square[i][2], square[i][3]
    minX = min(x1, x2)
    maxX = max(x1, x2)
    minY = min(y1, y2)
    maxY = max(y1, y2)

    for y in range(minY, maxY):
        for x in range(minX, maxX):
            matrix[y][x] = 1

for i in range(len(matrix)):
    result += sum(matrix[i])

print(result)
