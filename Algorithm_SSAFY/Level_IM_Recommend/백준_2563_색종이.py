import sys

sys.stdin = open("./input.txt", "r", encoding="utf-8")

n = int(input())

matrix = [[0] * 100 for _ in range(100)]

result = 0

for _ in range(n):
    p, q = map(int, input().split())
    for y in range(q, q+10):
        for x in range(p, p+10):
            matrix[y][x] = 1

for m in matrix:
    result += sum(m)

print(result)
