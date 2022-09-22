import sys
from collections import deque

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0812/input_1267.txt", "r", encoding='utf-8')

T = 10

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    inputList = list(map(int, input().split()))
    childList = [[] for _ in range(V+1)]
    parentList = [[] for _ in range(V+1)]
    rootNode = []
    visited = [False for _ in range(V+1)]
    q = deque()
    result = []

    # 부모 정보를 가진 배열 만들기
    for i in range(0, len(inputList) - 1, 2):
        parent = inputList[i]
        child = inputList[i+1]
        parentList[child].append(parent)
        childList[parent].append(child)

    # 루트 노드 찾기
    for i in range(1, len(parentList)):
        if not parentList[i]:
            rootNode.append(i)

    def checkParentNode(node):
        for i in parentList[node]:
            if visited[i]:
                continue
            else:
                return 0
        return 1

    # 루트 노드 순회하며 자식들 visited 찍기
    for i in rootNode:
        q.append(i)
        while q:
            p = q.popleft()
            result.append(p)
            visited[p] = True
            for c in childList[p]:
                if checkParentNode(c):
                    q.append(c)

    # 노드에 연결되지 않은 외딴 섬들 추가
    for i in range(1, V+1):
        if not visited[i]:
            result.append(i)

    print("#{}".format(test_case), end=" ")
    for i in result:
        print(i, end=" ")
    print()
