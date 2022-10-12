import sys
import copy
sys.stdin = open("input.txt", "r", encoding="UTF-8")

T = int(input())


def dfs(depth, arr, count):
    global minCount
    if count > minCount:
        return
    if depth == d:
        if check(arr) == w:
            minCount = min(minCount, count)
        return

    original = copy.deepcopy(arr)

    # 안 바꿈
    dfs(depth+1, arr, count)

    # A로 바꾸기
    for x in range(w):
        arr[depth][x] = 0
    dfs(depth+1, arr, count+1)
    arr = copy.deepcopy(original)

    # B로 바꾸기
    for x in range(w):
        arr[depth][x] = 1
    dfs(depth+1, arr, count+1)
    arr = copy.deepcopy(original)


def check(arr):
    check = [0 for _ in range(w)]
    for x in range(w):
        temp = []
        for y in range(d):
            if not temp:
                temp.append(arr[y][x])
            else:
                if temp[-1] == arr[y][x]:
                    temp.append(arr[y][x])
                else:
                    if len(temp) >= k:
                        check[x] = 1
                        break
                    temp = [arr[y][x]]
        if temp:
            if len(temp) >= k:
                check[x] = 1
        if check[x] < 1:
            return -1
    return sum(check)


for test_case in range(1, T+1):
    d, w, k = map(int, input().split())
    minCount = float('inf')
    matrix = [list(map(int, input().split())) for _ in range(d)]

    if (check(matrix) == w):
        print("#{} 0".format(test_case))
        continue

    dfs(0, matrix, 0)
    print(minCount)
