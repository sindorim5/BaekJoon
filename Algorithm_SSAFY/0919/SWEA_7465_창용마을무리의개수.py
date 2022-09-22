import sys
from collections import deque
sys.stdin = open("0919/창용마을.txt", "r", encoding="UTF-8")

T = int(input())


def bfs(i):
    global count
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        node = q.popleft()
        for element in graph[node]:
            if not visited[element]:
                visited[element] = True
                q.append(element)


for test_case in range(1, T+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    count = 0
    visited = [False for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            count += 1

    print("#{} {}".format(test_case, count))
