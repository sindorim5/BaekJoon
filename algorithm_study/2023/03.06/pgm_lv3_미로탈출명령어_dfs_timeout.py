import sys

sys.setrecursionlimit(10**8)

# d l r u
# 하 좌 우 상, 알파벳 순으로 탐색
# 탐색 성공하면 최단 거리
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
letter = ["d", "l", "r", "u"]
answer = "impossible"


def dfs(depth, trace, nowX, nowY, n, m, r, c, k):
    global answer
    # answer가 값이 있으면 dfs 탈출
    if answer != "impossible":
        return

    if (depth == k-1):
        if (nowX == r-1 and nowY == c-1):
            # trace 해독
            temp = ""
            for num in trace:
                temp += letter[num]
            answer = temp
        return

    for i in range(4):
        nX = nowX + dx[i]
        nY = nowY + dy[i]
        if (0 <= nX < n and 0 <= nY < m):
            dfs(depth + 1, trace + [i], nX, nY, n, m, r, c, k)


def solution(n, m, x, y, r, c, k):
    global answer

    # 이거 넣으면 답도 틀림;;;;
    distance = abs(x - r) + abs(y - r)
    if distance > k or (k - distance) % 2 == 1:
        return "impossible"

    dfs(0, [], x-1, y-1, n, m, r, c, k)

    # dfs 나와서도 answer가 없으면 impossible로

    return answer
