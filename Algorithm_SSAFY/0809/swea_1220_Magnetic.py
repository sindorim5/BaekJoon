import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        y, x = 0, i
        flag = 0
        while y < N:
            if not flag and matrix[y][x] == 1:
                flag = 1
            elif flag and matrix[y][x] == 2:
                flag = 0
                count += 1
            y += 1

    print("#{} {}".format(test_case, count))
