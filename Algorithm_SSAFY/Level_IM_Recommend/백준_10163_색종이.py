import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

n = int(input())
matrix = [[0] * 1001 for _ in range(1001)]
for i in range(n):
    x, y, w, h = map(int, input().split())
    for q in range(y, y + h):
        for p in range(x, x + w):
            matrix[q][p] = i + 1

for i in range(n):
    count = 0
    for m in matrix:
        count += m.count(i + 1)
    print(count)
