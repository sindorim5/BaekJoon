import sys
import copy
sys.stdin = open("input.txt", "r", encoding="UTF-8")

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

cctvList = [[],
[[0], [1], [2], [3]],
[[0, 1], [2, 3]],
[[0, 3], [1, 3], [1, 2], [0, 2]],
[[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
[[0, 1, 2, 3]]
]

n, m = map(int, input().split())
matrix = []
cctvLoc = []
minCount = 10**9

for y in range(n):
    temp = list(map(int, input().split()))
    for x in range(m):
        if 1 <= temp[x] <= 5:
            cctvLoc.append((y, x))
    matrix.append(temp)

cctvCount = len(cctvLoc)

def countZero(matrix):
    count = 0
    for y in range(n):
        for x in range(m):
            if matrix[y][x] == 0:
                count += 1
    return count

def watch(y, x, d, arr):
    nY = y + dy[d]
    nX = x + dx[d]
    while 0 <= nY < n and 0 <= nX < m:
        if arr[nY][nX] == 0 or arr[nY][nX] == 9:
            arr[nY][nX] = 9
        elif arr[nY][nX] == 6:
            break
        nY += dy[d]
        nX += dx[d]
    return arr

def dfs(depth, arr):
    global minCount
    if depth == cctvCount:
        minCount = min(minCount, countZero(arr))
        return

    y, x = cctvLoc[depth][0], cctvLoc[depth][1]
    type = arr[y][x]
    original = copy.deepcopy(arr)

    for directions in cctvList[type]:
        for d in directions:
            arr = watch(y, x, d, arr)
        dfs(depth+1, arr)
        arr = copy.deepcopy(original)

dfs(0, matrix)

print(minCount)


