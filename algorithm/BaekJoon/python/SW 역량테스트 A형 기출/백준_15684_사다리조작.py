import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")

input = sys.stdin.readline

n, m, h = map(int, input().split())

matrix = [[0 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1

result = 999999999


def down(arr):
    i = 0
    while i < n:
        temp = i
        for y in range(h):
            if arr[y][temp]:
                temp += 1
            elif temp > 0 and arr[y][temp - 1]:
                temp -= 1
        if temp == i:
            i += 1
            continue
        else:
            return False
    return True


def dfs(count, y, x):
    global result
    if result <= count:
        return
    if down(matrix):
        result = min(result, count)
        return
    if count == 3:
        return
    for nY in range(y, h):
        if nY == y:
            idx = x
        else:
            idx = 0
        for nX in range(idx, n-1):
            if matrix[nY][nX] == 0:
                matrix[nY][nX] = 1
                dfs(count + 1, nY, nX + 2)
                matrix[nY][nX] = 0


dfs(0, 0, 0)

if result <= 3:
    print(result)
else:
    print(-1)
