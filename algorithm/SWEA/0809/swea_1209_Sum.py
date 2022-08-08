import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    maxSum = 0

    matrix = [list(map(int, input().split())) for _ in range(100)]

    for y in range(100):
        sum = 0
        for x in range(100):
            sum += matrix[y][x]
        maxSum = max(maxSum, sum)

    for x in range(100):
        sum = 0
        for y in range(100):
            sum += matrix[y][x]
        maxSum = max(maxSum, sum)

    sum = 0
    for i in range(100):
        sum += matrix[i][i]
    maxSum = max(maxSum, sum)

    sum = 0
    for i in range(100):
        sum += matrix[i][99 - i]
    maxSum = max(maxSum, sum)

    print(f"#{test_case} {maxSum}")
