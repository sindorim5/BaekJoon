import sys

sys.stdin = open("0929/숫자만들기.txt", "r", encoding="UTF-8")

T = int(input())


def dfs(depth, idx, result):
    global maxValue, minValue
    if (depth == n-1):
        arr.append(result)
        return

    for i in range(4):
        if opList[i]:
            opList[i] -= 1
            if i == 0:
                dfs(depth+1, idx+1, result+inputList[idx])
            elif i == 1:
                dfs(depth+1, idx+1, result-inputList[idx])
            elif i == 2:
                dfs(depth+1, idx+1, result*inputList[idx])
            elif i == 3:
                if result < 0:
                    temp = -1 * (abs(result) // inputList[idx])
                else:
                    temp = result // inputList[idx]
                dfs(depth+1, idx+1, temp)
            opList[i] += 1
        else:
            continue


for test_case in range(1, T+1):
    n = int(input())
    arr = []
    opList = list(map(int, input().split()))
    inputList = list(map(int, input().split()))

    maxValue = -999999999
    minValue = 10**9
    dfs(0, 1, inputList[0])

    print("#{} {}".format(test_case, max(arr)-min(arr)))
