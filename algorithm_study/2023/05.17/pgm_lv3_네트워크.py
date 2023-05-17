def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        # 방문하지 않았다면?
        if visited[i] == False:
            # dfs를 들어가서 최대한 네트워크를 연결하고 +1
            dfs(n, computers, i, visited)
            answer += 1 
    return answer

def dfs(n, computers, idx, visited):
    visited[idx] = True
    for j in range(n):
        # 연결되어 있고 방문하지 않았다면?
        if computers[idx][j] == 1 and visited[j] == False:
            dfs(n, computers, j, visited)