import sys
from collections import deque
sys.stdin = open("0920/탈주범검거.txt", "r", encoding="UTF-8")

T = int(input())

# 상 하 좌 우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 터널 구조물 타입
dir = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]

# 반대 방향
counter = [1, 0, 3, 2]


def bfs(y, x):
    q = deque()
    depth = 2
    q.append([y, x, depth])
    visited[y][x] = 1
    while q:
        nowY, nowX, nowDepth = q.popleft()
        pipe = matrix[nowY][nowX]
        for i in dir[pipe]:
            nY = nowY + delta[i][0]
            nX = nowX + delta[i][1]
            if 0 <= nY < n and 0 <= nX < m:
                if matrix[nY][nX] == 0:
                    continue
                if not visited[nY][nX]:
                    nextPipe = matrix[nY][nX]
                    if counter[i] in dir[nextPipe]:
                        visited[nY][nX] = nowDepth
                        if nowDepth < l:
                            q.append([nY, nX, nowDepth+1])


for test_case in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    bfs(r, c)

    count = 0
    for y in range(n):
        for x in range(m):
            if 0 < visited[y][x] <= l:
                count += 1

    print("#{} {}".format(test_case, count))
