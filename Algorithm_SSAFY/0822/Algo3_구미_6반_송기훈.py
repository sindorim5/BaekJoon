from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    # 시작점 찾기
    def findStart():
        for y in range(N):
            for x in range(N):
                if matrix[y][x] == 2:
                    return (y, x)

        return (0, 0)

    startY, startX = findStart()

    def bfs(depth, y, x):
        q = deque()
        q.append((depth, y, x))
        visited[y][x] = True

        while q:
            depth, y, x = q.popleft()

            # 도착지에 도달하면 거리(depth)를 return
            if matrix[y][x] == 3:
                return depth

            # for문을 돌면서 q에 4방향을 탐색한다
            for i in range(4):
                nY = y + dy[i]
                nX = x + dx[i]

                # 다음 후보가 NxN 범위에 있고 가보지 않은 곳이고 벽이 아니라면 큐에 추가한다.
                if 0 <= nY < N and 0 <= nX < N and visited[nY][nX] == False:
                    if matrix[nY][nX] != 1:
                        visited[nY][nX] = True
                        q.append((depth + 1, nY, nX))

    result = bfs(1, startY, startX)
    print("#{} {}".format(test_case, result))
