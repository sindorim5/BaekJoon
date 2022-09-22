import sys
sys.stdin = open("0921/프로세서.txt", "r", encoding="UTF-8")

T = int(input())

# 상 하 좌 우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def connectTest(y, x):
    candidate = [0,0,0,0]
    for i in range(4):
        nY = y + delta[i][0]
        nX = x + delta[i][1]
        count = 0
        while 0 <= nY < n and 0 <= nX < n:
            if matrix[nY][nX]:
                break
            nY += delta[i][0]
            nX += delta[i][1]
            count += 1
        else: candidate[i] = count
    return candidate

def connect(y, x, i):
    nY = y + delta[i][0]
    nX = x + delta[i][1]
    while 0 <= nY < n and 0 <= nX < n:
        if matrix[nY][nX] == 0:
            matrix[nY][nX] = 9
            nY += delta[i][0]
            nX += delta[i][1]

def disconnect(y, x, i):
    nY = y + delta[i][0]
    nX = x + delta[i][1]
    while 0 <= nY < n and 0 <= nX < n:
        if matrix[nY][nX] == 9:
            matrix[nY][nX] = 0
            nY += delta[i][0]
            nX += delta[i][1]

def dfs(depth, connected, line):
    global minValue, maxConn
    if depth == coreCount:
        if maxConn == connected:
            minValue = min(minValue, line)
        if maxConn < connected:
            maxConn = connected
            minValue = line
        return
    candidate = connectTest(coreList[depth][0], coreList[depth][1])
    for dir in range(4):
        if candidate[dir] == 0:
            continue
        connect(coreList[depth][0], coreList[depth][1], dir)
        dfs(depth + 1, connected + 1, line + candidate[dir])
        disconnect(coreList[depth][0], coreList[depth][1], dir)
    dfs(depth + 1, connected, line)

for test_case in range(1, T+1):
    n = int(input())
    minValue = 10**9
    maxConn = -999999
    coreList = []
    matrix = []
    for y in range(n):
        temp = list(map(int, input().split()))
        for x in range(n):
            if y == 0 or y == n-1 or x == 0 or x == n-1:
                continue
            if temp[x] == 1:
                coreList.append((y,x))
        matrix.append(temp)
    coreCount = len(coreList)
    dfs(0, 0, 0)

    print("#{} {}".format(test_case, minValue))