import sys

sys.stdin = open("input.txt", "r", encoding="UTF-8")

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x, depth, flag):
    global maxRoad
    maxRoad = max(depth, maxRoad)

    for i in range(4):
        nY = y + dy[i]
        nX = x + dx[i]
        if 0 <= nY < n and 0 <= nX < n:
            # 가지 않은 곳일 때
            if visited[nY][nX] == False:
                # 공사를 안해도 되는 곳일 때
                if matrix[y][x] > matrix[nY][nX]:
                    visited[nY][nX] = True
                    dfs(nY, nX, depth+1, flag)
                    visited[nY][nX] = False
                # 공사가 필요한 곳일 때
                else:
                    # 공사를 아직 하지 않았다면
                    if flag == False:
                        for d in range(1, k+1):
                            if matrix[y][x] > (matrix[nY][nX] - d):
                                visited[nY][nX] = True
                                matrix[nY][nX] -= d
                                dfs(nY, nX, depth+1, True)
                                visited[nY][nX] = False
                                matrix[nY][nX] += d
                    else:
                        continue


for test_case in range(1, T+1):
    n, k = map(int, input().split())
    matrix = []
    maxLoc = []
    maxRoad = -1
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    visited = [[False for _ in range(n)] for _ in range(n)]

    maxValue = max(map(max, matrix))

    for y in range(n):
        for x in range(n):
            if matrix[y][x] == maxValue:
                maxLoc.append((y, x))

    for m in maxLoc:
        visited[m[0]][m[1]] = True
        dfs(m[0], m[1], 1, False)
        visited[m[0]][m[1]] = False

    print("#{} {}".format(test_case, maxRoad))
