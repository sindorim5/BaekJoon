import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10

for test_case in range(1, T + 1):
    N = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    y = 99
    x = ladder[y].index(2)
    flag = 0

    while y > 0:
        if (flag == 0 or flag == 1) and (x > 0) and ladder[y][x - 1] == 1:
            x -= 1
            flag = 1
        elif (flag == 0 or flag == 2) and (x < 99) and ladder[y][x + 1] == 1:
            x += 1
            flag = 2
        else:
            y -= 1
            flag = 0

    print("#{} {}".format(N, x))
