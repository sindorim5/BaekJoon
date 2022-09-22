import sys
from collections import deque

sys.stdin = open("공통조상.txt", "r", encoding="UTF-8")

T = int(input())

for test_case in range(1, T+1):
    v, e, a, b = map(int, input().split())
    inputList = list(map(int, input().split()))
    parentList = [[] for _ in range(v + 1)]
    childList = [[] for _ in range(v + 1)]
    for i in range(0, len(inputList), 2):
        parentList[inputList[i + 1]].append(inputList[i])
        childList[inputList[i]].append(inputList[i + 1])

    # a의 간선
    q = deque()
    aParent = []
    q.append(a)
    while q:
        nowA = q.popleft()
        if parentList[nowA]:
            nextA = parentList[nowA][0]
            q.append(nextA)
            aParent.append(nextA)

    # b의 간선
    q = deque()
    bParent = []
    q.append(b)
    while q:
        nowB = q.popleft()
        if parentList[nowB]:
            nextB = parentList[nowB][0]
            q.append(nextB)
            bParent.append(nextB)

    # 공통부모찾기
    parent = -1
    for i in range(len(aParent)):
        for j in range(len(bParent)):
            if aParent[i] == bParent[j]:
                parent = aParent[i]
        if parent > 0:
            break

    # 서브트리찾기
    q = deque()
    subTree = [parent]
    q.append(parent)
    while q:
        now = q.popleft()
        for child in childList[now]:
            if child not in q:
                q.append(child)
            if child not in subTree:
                subTree.append(child)

    print("#{} {} {}".format(test_case, parent, len(subTree)))
