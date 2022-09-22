import sys

sys.stdin = open("0916/벌꿀채취.txt", "r", encoding="UTF-8")

T = int(input())

def cal(arr):
    value = 0
    result = []
    # c보다 작으면 그냥 계산 후 return
    if sum(arr) <= c:
        for i in arr:
            value += i * i
        return value

    # 부분집합 만들고 결과값 구하기
    def dfs(depth, nowArr):
        if depth == m:
            if sum(nowArr) <= c:
                temp = 0
                for e in nowArr:
                    temp += e * e
                result.append(temp)
            return
        dfs(depth+1, nowArr + [arr[depth]])
        dfs(depth+1, nowArr)
    
    dfs(0, [])
    if result:
        return max(result)
    else:
        return 0

def pick(y, x):
    global maxValue
    visited = [[False] * n for _ in range(n)]
    aList = []
    bLists = []
    for i in range(m):
        visited[y][x+i] = True
        aList.append(matrix[y][x+i])
    # bLists 만들기
    for y2 in range(n):
        for x2 in range(n-m+1):
            # 이미 사용된 점이면 제외
            if [y2, x2] in banList:
                continue
            # aList에서 사용된 점이 아니라면
            if not visited[y2][x2]:
                dx2 = x2 + m - 1
                if 0 <= dx2 < n:
                    bList = []
                    for i in range(m):
                        bList.append(matrix[y2][x2+i])
                    bLists.append(bList)
    aMax = cal(aList)
    for bList in bLists:
        bMax = cal(bList)
        maxValue = max(maxValue, aMax+bMax)


for test_case in range(1, T+1):
    n, m, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    banList = []
    maxValue = -999
    for y in range(n):
        for x in range(n-m+1):
            banList.append([y, x])
            pick(y, x)

    print("#{} {}".format(test_case, maxValue))