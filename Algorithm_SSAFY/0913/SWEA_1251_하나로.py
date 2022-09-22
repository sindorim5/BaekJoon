import sys

sys.stdin = open("./0913/하나로.txt", "r", encoding="UTF-8")

T = int(input())


def prim(idx):
    visited = [False] * n
    cost = [float('inf')] * n

    cost[idx] = 0

    for _ in range(n-1):
        v = 0
        minValue = float('inf')
        # 배열을 순회하면서 minValue를 선택
        for i in range(n):
            if not visited[i]:
                if cost[i] < minValue:
                    v = i
                    minValue = cost[i]
        # minValue인 노드 값을 방문표시해서 고정
        visited[v] = True
        for j in range(n):
            if not visited[j]:
                # 방문하지 않은 노드를 순회하며
                # 이전 노드, minValue 노드와 거리 중 최솟값을 마킹
                cost[j] = min(cost[j], distance[v][j])

    return sum(cost)


for test_case in range(1, T+1):
    n = int(input())
    xList = list(map(int, input().split()))
    yList = list(map(int, input().split()))
    e = float(input())

    distance = [[0] * n for _ in range(n)]

    # a와 b의 거리의 제곱을 저장
    for a in range(n):
        for b in range(a, n):
            temp = (yList[a] - yList[b])**2 + (xList[a] - xList[b])**2
            distance[a][b] = temp
            distance[b][a] = temp

    print("#{} {}".format(test_case, round(prim(0) * e)))
