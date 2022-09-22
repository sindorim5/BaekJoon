from collections import deque

inputList = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
graph = [[] for _ in range(8)]
for i in range(0, len(inputList), 2):
    graph[inputList[i]].append(inputList[i+1])

visited = [False for _ in range(8)]

q = deque()
q.append(1)
result = [1]
while q:
    node = q.popleft()
    for child in graph[node]:
        if not visited[child]:
            result.append(child)
            visited[child] = True
            q.append(child)

print("-".join(map(str, result)))
