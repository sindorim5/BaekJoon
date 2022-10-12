from collections import deque

n = int(input())


numbers = [i for i in range(1, n+1)]
population = [0]

population += list(map(int, input().split()))

graph = [[]]
combination = []
minDiff = 10**9

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp[1:])


def dfs(depth, arr):
    if depth == n:
        if arr != [] and arr not in combination:
            combination.append(arr)
        return

    dfs(depth+1, arr)

    dfs(depth+1, arr + [numbers[depth]])


def bfs(arr):
    q = deque()
    q.append(arr[0])
    checkList = [arr[0]]
    while q:
        element = q.popleft()
        for x in graph[element]:
            if x in arr and x not in checkList:
                q.append(x)
                checkList.append(x)
        if len(checkList) == len(arr):
            return True
    return False


def checkDiff(arr1, arr2):
    global minDiff
    pop1 = 0
    pop2 = 0
    for x in arr1:
        pop1 += population[x]

    for x in arr2:
        pop2 += population[x]
    diff = abs(pop1-pop2)
    minDiff = min(diff, minDiff)


dfs(0, [])

combination.sort(key=lambda x: len(x))

for i in range(len(combination)-1 // 2):
    team = combination[i]
    otherTeam = []
    for x in numbers:
        if x not in team:
            otherTeam.append(x)

    if len(team) > 0 and len(otherTeam) > 0:
        if bfs(team) and bfs(otherTeam):
            checkDiff(team, otherTeam)

if minDiff == 10**9:
    print(-1)
else:
    print(minDiff)
