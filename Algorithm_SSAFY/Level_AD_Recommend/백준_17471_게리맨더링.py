import sys
from collections import deque

sys.stdin = open("input.txt", "r", encoding="utf-8")

n = int(input())
minValue = 999999999

# area만큼 count가 되면 연결된 지역이므로 bfs 돌면서 합한 인구 수 return


def bfs(area):
    q = deque()
    visited = [False] * (n + 1)
    tempPopulation = 0
    count = 1

    q.append(area[0])
    visited[area[0]] = True
    while q:
        node = q.popleft()
        tempPopulation += population[node]
        for child in graph[node]:
            if child in area and visited[child] == False:
                visited[child] = True
                count += 1
                q.append(child)
    if count == len(area):
        return tempPopulation


# target 만큼 고르고 인구수 차이 return
def dfs(target, pick, idx):
    global minValue
    if pick == target:
        area1 = []
        area2 = []
        for i in range(1, n + 1):
            if visited[i]:
                area1.append(i)
            else:
                area2.append(i)
        a = bfs(area1)
        b = bfs(area2)
        if a and b:
            minValue = min(abs(a - b), minValue)
        return

    for i in range(idx, n + 1):
        visited[i] = True
        dfs(target, pick + 1, i + 1)
        visited[i] = False


population = [0] + list(map(int, input().split()))
graph = [[]]

for _ in range(n):
    temp = list(map(int, input().split()))
    temp.pop(0)
    graph.append(temp)

for i in range(1, n // 2 + 1):
    visited = [False for _ in range(n + 1)]
    dfs(i, 0, 1)

if minValue == 999999999:
    print(-1)
else:
    print(minValue)
