import sys
from collections import deque
sys.stdin = open("화학물질2.txt", "r", encoding="UTF-8")

T = int(input())

# 하, 우
dy = [1, 0]
dx = [0, 1]


def bfs(y, x):
    global points
    temp = [[y, x]]
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        nowY, nowX = q.popleft()
        for i in range(2):
            nY = nowY + dy[i]
            nX = nowX + dx[i]
            if 0 <= nY < n and 0 <= nX < n and not visited[nY][nX] and matrix[nY][nX] > 0:
                visited[nY][nX] = True
                q.append((nY, nX))
                temp.append([nY, nX])
    points.append([temp[0], temp[-1]])


for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    points = []
    arrays = []
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and matrix[y][x] > 0:
                bfs(y, x)

    for point in points:
        diffY = abs(point[0][0] - point[1][0]) + 1
        diffX = abs(point[0][1] - point[1][1]) + 1
        arrays.append([diffY, diffX])

    connection = [arrays.pop(0)]

    i = 0
    while arrays:
        # 연결의 앞쪽에 추가
        if arrays[i][1] == connection[0][0]:
            connection.insert(0, arrays.pop(i))
            i = 0
        # 연결의 뒷쪽에 추가
        elif arrays[i][0] == connection[-1][1]:
            connection.append(arrays.pop(i))
            i = 0
        else:
            i += 1

    size = len(connection)
    dimension = []
    DP = [[0] * size for _ in range(size)]
    for conn in connection:
        dimension.append(conn[0])
    dimension.append(connection[-1][1])
    for delta in range(1, size):
        for i in range(size-delta):
            j = i + delta
            DP[i][j] = 10**9
            for k in range(i, j):
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k+1][j] +
                               dimension[i-1] * dimension[k] * dimension[j])
    print("#{} {}".format(test_case, DP[0][size-1]))
    # Matrix chain multiplication
    # https://blog.naver.com/babobigi/220535210931
