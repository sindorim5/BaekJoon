import sys
import copy
sys.stdin = open("input.txt", "r", encoding="UTF-8")

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

statusList = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [
    2, 3], [3, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]
cctvList = []
minCount = 100

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def countZero(temp):
    count = 0
    for y in range(n):
        for x in range(m):
            if temp[y][x] == 0:
                count += 1
    return count


for y in range(n):
    for x in range(m):
        if matrix[y][x] == 0 or matrix[y][x] == 6:
            continue
        else:
            cctvList.append((matrix[y][x], y, x))


def paintZero(arr, status, y, x):
    for s in status:
        tempY = y
        tempX = x
        while True:
            tempY += dy[s]
            tempX += dx[s]
            if tempY < 0 or tempX < 0 or tempY >= n or tempX >= m:
                break
            if arr[tempY][tempX] == 6:
                break
            elif arr[tempY][tempX] == 0:
                arr[tempY][tempX] = 9


def dfs(depth, arr):
    global minCount
    if depth == len(cctvList):
        count = countZero(arr)
        if minCount > count:
            minCount = count
        return

    tempMatrix = copy.deepcopy(arr)
    cctv, y, x = cctvList[depth]
    for status in statusList[cctv]:
        paintZero(tempMatrix, status, y, x)
        dfs(depth + 1, tempMatrix)
        tempMatrix = copy.deepcopy(arr)


dfs(0, matrix)
print(minCount)
