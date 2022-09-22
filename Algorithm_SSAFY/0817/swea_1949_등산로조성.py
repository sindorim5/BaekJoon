import sys

sys.stdin = open("0817/1949_input.txt", "r", encoding="utf-8")

moveList = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(y, x, path, flag):
    global maxPath
    if maxPath < path:
        maxPath = path
    for dy, dx in moveList:
        nY = y + dy
        nX = x + dx
        # 영역을 벗어나면 continue
        if nY < 0 or nY >= n or nX < 0 or nX >= n:
            continue
        if visited[nY][nX] == True:
            continue
        # 이동
        if matrix[y][x] > matrix[nY][nX]:
            visited[nY][nX] = True
            dfs(nY, nX, path + 1, flag)
            visited[nY][nX] = False
        # 이동이 불가능하지만 공사를 안한 경우
        elif matrix[y][x] <= matrix[nY][nX] and not flag:
            # 공사할 수 있는 모든 경우
            for i in range(1, k + 1):
                matrix[nY][nX] -= i
                flag = True
                if matrix[y][x] > matrix[nY][nX]:
                    visited[nY][nX] = True
                    dfs(nY, nX, path + 1, flag)
                    visited[nY][nX] = False
                # 공사 취소하기 -> 다른 경우를 체크하기 위해
                flag = False
                matrix[nY][nX] += i


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    maxList = []
    maxValue = max(list(map(max, matrix)))
    maxPath = 0

    for y in range(n):
        for x in range(n):
            if matrix[y][x] == maxValue:
                visited = [[False] * n for _ in range(n)]
                visited[y][x] = True
                dfs(y, x, 1, False)

    print("#{} {}".format(test_case, maxPath))
