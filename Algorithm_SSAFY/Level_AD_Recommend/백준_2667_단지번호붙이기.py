import sys
from collections import deque

sys.stdin = open("C:/SSAFY/clone/Algorithm_SSAFY/input.txt",
                 "r", encoding="utf-8")
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
result = []


def bfs(y, x):
    q = deque()
    q.append((y, x))
    count = 1
    while q:
        nowY, nowX = q.popleft()
        visited[nowY][nowX] = True
        for i in range(4):
            nY = nowY + dy[i]
            nX = nowX + dx[i]
            if 0 <= nY < n and 0 <= nX < n and visited[nY][nX] == False and matrix[nY][nX] == 1:
                if (nY, nX) not in q:
                    count += 1
                    q.append((nY, nX))
    return count


for y in range(n):
    for x in range(n):
        if matrix[y][x] == 1 and visited[y][x] == False:
            result.append(bfs(y, x))

print(len(result))
result.sort()
for r in result:
    print(r)
