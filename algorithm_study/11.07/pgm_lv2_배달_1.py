def solution(N, road, K):
    graph = [[10**9 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        graph[i][i] = 0

    for a, b, c in road:
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer = [x for x in graph[1] if x <= K]
    return len(answer)


# https://velog.io/@minji0801/%EC%98%A4%EB%8B%B5%EB%85%B8%ED%8A%B8%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%B0%EB%8B%AC-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C
