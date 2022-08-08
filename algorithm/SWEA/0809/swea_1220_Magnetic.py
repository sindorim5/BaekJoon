import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        y, x = 0, i
        q = deque()
        while y < N:
            if not q and matrix[y][x] == 1:
                q.append(1)
            elif q and matrix[y][x] == 2:
                q.popleft()
                count += 1
            y += 1

    print(f"#{test_case} {count}")
