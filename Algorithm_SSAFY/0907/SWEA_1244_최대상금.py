import sys

sys.stdin = open("./0907/최대상금.txt", "r", encoding="UTF-8")
T = int(input())


def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def dfs(depth, arr):
    global result, resultList
    if depth == change:
        temp = int("".join(arr))
        if result < temp:
            result = temp
        return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            temp = int("".join(arr))
            if (temp, depth) not in resultList:
                resultList.append((temp, depth))
                dfs(depth+1, arr)
            arr[i], arr[j] = arr[j], arr[i]


for test_case in range(1, T+1):
    numList, change = map(int, input().split())
    numList = list(str(numList))
    resultList = []
    result = -999999999
    dfs(0, numList)
    print("#{} {}".format(test_case, result))
