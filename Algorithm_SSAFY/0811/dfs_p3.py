# input
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

inputList = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

link = [[] for _ in range(8)]
result = []

visited = [False for _ in range(8)]

for i in range(0, len(inputList) - 1, 2):
    a = inputList[i]
    b = inputList[i + 1]
    link[a].append(b)


def dfs(n):
    visited[n] = True
    result.append(n)
    for i in link[n]:
        if visited[i] == False:
            dfs(i)


dfs(1)

for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i])
    else:
        print(result[i], end="-")
