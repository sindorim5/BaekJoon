import sys

sys.stdin = open("input.txt", "r", encoding="UTF-8")

T = int(input())

dy = [-1, 1, 1, -1]
dx = [1, 1, -1, -1]


def makeDiamonds(y, x, dir, path, desserts):
    global maxValue

    nY = y + dy[dir]
    nX = x + dx[dir]

    if dir == 3 and path[0] == (nY, nX):
        maxValue = max(maxValue, len(desserts))
        return
    # 직진
    if 0 <= nY < n and 0 <= nX < n:
        if matrix[nY][nX] not in desserts:
            makeDiamonds(nY, nX, dir, path +
                         [(nY, nX)], desserts + [matrix[nY][nX]])

    # 방향 전환
    if dir < 3:
        nY = y + dy[dir+1]
        nX = x + dx[dir+1]
        if 0 <= nY < n and 0 <= nX < n:
            if dir == 2 and path[0] == (nY, nX):
                maxValue = max(maxValue, len(desserts))
                return
            if matrix[nY][nX] not in desserts:
                makeDiamonds(nY, nX, dir+1, path +
                             [(nY, nX)], desserts + [matrix[nY][nX]])


for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    maxValue = 0
    for y in range(n):
        for x in range(n):
            makeDiamonds(y, x, 0, [(y, x)], [matrix[y][x]])

    if maxValue == 0:
        print("#{} -1".format(test_case))
    else:
        print("#{} {}".format(test_case, maxValue))
