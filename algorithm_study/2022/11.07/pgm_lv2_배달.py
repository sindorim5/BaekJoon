from collections import deque

def solution(N, road, K):
    answer = [1]
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for a,b,c in road:
        if graph[a][b] == 0:
            graph[a][b] = c
            graph[b][a] = c
        else:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)

    visited = [False for _ in range(N+1)]
    q = deque()
    q.append([1, 0])
    while q:
        now, nowDist = q.popleft()
        visited[now] = True
        for i in range(1, N+1):
            if i == now:
                continue
            distance = graph[now][i]
            if distance == 0:
                continue
            if not visited[i]:
                if distance + nowDist <= K:
                    q.append([i, distance+nowDist])
                    if i not in answer:
                        answer.append(i)

    return len(answer)
