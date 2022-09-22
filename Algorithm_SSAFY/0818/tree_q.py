# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

n = 13
inputList = [
    1,
    2,
    1,
    3,
    2,
    4,
    3,
    5,
    3,
    6,
    4,
    7,
    5,
    8,
    5,
    9,
    6,
    10,
    6,
    11,
    7,
    12,
    11,
    13,
]

graph = [[] for _ in range(14)]

print(graph)

for i in range(0, len(inputList), 2):
    graph[inputList[i]].append(inputList[i + 1])


def tree(i):
    print(i, end=" ")
    if graph[i]:
        for element in graph[i]:
            tree(element)


tree(1)
