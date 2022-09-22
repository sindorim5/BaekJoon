# pypy 통과 python 통과
import sys
from collections import deque

sys.stdin = open("input.txt", "r", encoding="utf-8")
input = sys.stdin.readline


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
answer = 0


def bfs(q):
    cnt = -1
    visited = [[False for _ in range(m)] for _ in range(n)]
    y, x = q[0]
    visited[y][x] = True

    while q:
        cnt += 1
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                nY = y + dy[i]
                nX = x + dx[i]
                if (
                    0 <= nY < n
                    and 0 <= nX < m
                    and matrix[nY][nX] == "L"
                    and not visited[nY][nX]
                ):
                    q.append([nY, nX])
                    visited[nY][nX] = True

    return cnt


def check():
    global answer
    for y in range(n):
        for x in range(m):
            if matrix[y][x] == "L":
                num = 0
                for i in range(4):
                    nY = y + dy[i]
                    nX = x + dx[i]
                    if 0 <= nY < n and 0 <= nX < m and matrix[nY][nX] == "L":
                        num += 1
                if 0 < num <= 2:
                    cnt = bfs(deque([[y, x]]))
                    answer = max(answer, cnt)


check()
print(answer)
