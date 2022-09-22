import sys
from collections import deque

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0817/1861_input.txt", "r", encoding="utf-8")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    maxCount = 0
    result = []

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    def bfs(nowY, nowX):
        q = deque()
        q.append((nowY, nowX))
        count = 1
        while q:
            tempY, tempX = q.popleft()
            for i in range(4):
                nY = tempY + dy[i]
                nX = tempX + dx[i]
                if (0 <= nY < n and 0 <= nX < n and matrix[nY][nX] == (matrix[tempY][tempX] + 1)):
                    count += 1
                    q.append((nY, nX))
        return count

    for y in range(n):
        for x in range(n):
            count = bfs(y, x)
            if maxCount < count:
                maxCount = count
                result = [matrix[y][x], maxCount]
            elif maxCount == count:
                result[0] = min(result[0], matrix[y][x])

    print("#{} {} {}".format(test_case, result[0], result[1]))
