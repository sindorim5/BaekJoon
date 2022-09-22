import sys
from collections import deque
sys.stdin = open("0919/사람네트워크2.txt", "r", encoding="UTF-8")


T = int(input())

MAXDIST = 10**9


def bfs(i):
    global minValue
    visited = [False for _ in range(n)]
    q = deque()
    depth = 1
    visited[i] = True
    depthList[i][i] = 0
    q.append([i, depth])
    while q:
        node, nowDepth = q.popleft()
        if sum(depthList[i]) > minValue:
            break
        for j in range(n):
            if j == i:
                continue
            if graph[node][j]:
                if not visited[j]:
                    visited[j] = True
                    q.append([j, nowDepth+1])
                    if not depthList[i][j]:
                        depthList[i][j] = nowDepth
                        depthList[j][i] = nowDepth
    return sum(depthList[i])


for test_case in range(1, T+1):
    inputList = list(map(int, input().split()))
    n = inputList[0]
    graph = []
    distance = [0 for _ in range(n)]
    depthList = [[0 for _ in range(n)] for _ in range(n)]
    minValue = MAXDIST
    idx = 1
    for i in range(n):
        temp = []
        for _ in range(n):
            temp.append(inputList[idx])
            idx += 1
        graph.append(temp)

    for i in range(n):
        distance[i] = bfs(i)
        minValue = min(minValue, distance[i])

    print("#{} {}".format(test_case, minValue))
