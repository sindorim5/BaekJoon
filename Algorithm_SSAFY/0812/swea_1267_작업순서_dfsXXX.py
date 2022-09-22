import sys
sys.setrecursionlimit(10**9)
sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0812/input_1267.txt", "r", encoding='utf-8')

T = 1

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    inputList = list(map(int, input().split()))
    parentList = [[] for _ in range(V+1)]
    childList = [[] for _ in range(V+1)]
    rootNode = []
    visited = [False for _ in range(V+1)]
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

    def dfs(node):
        result.append(node)
        visited[node] = True
        for i in childList[node]:
            # parent가 모두 visited이면 dfs
            if checkParentNode(i):
                dfs(i)

    for root in rootNode:
        dfs(root)

    # 노드에 연결되지 않은 외딴 섬들 추가
    for i in range(1, V+1):
        if not visited[i]:
            result.append(i)

    print("#{}".format(test_case), end=" ")
    for i in result:
        print(i, end=" ")
    print()
