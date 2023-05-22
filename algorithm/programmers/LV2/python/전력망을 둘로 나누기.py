from collections import deque


def solution(n, wires):
    answer = float('inf')

    connect = [True for _ in range(n-1)]

    for i in range(n-1):
        # 연결을 끊고 둘 중 한 노드를 시작으로 BFS
        connect[i] = False
        result = bfs(wires[i][1], connect, wires, n)
        answer = min(abs(n - 2 * len(result)), answer)
        connect[i] = True

    return answer


def bfs(start, connect, wires, n):
    result = [start]
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        visited[node] = True

        for i in range(len(wires)):
            # 연결되어 있고 노드가 포함되어 있다면?
            if connect[i] and node in wires[i]:
                # 들린 적이 없다면 deque와 result에 추가
                for element in wires[i]:
                    if not visited[element]:
                        q.append(element)
                        result.append(element)
    return result
