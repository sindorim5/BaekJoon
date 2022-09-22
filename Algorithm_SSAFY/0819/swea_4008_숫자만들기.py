import sys

sys.stdin = open("0819/4008_input.txt", "r", encoding="utf-8")

input = sys.stdin.readline

T = int(input())


def dfs(index, result):
    global maxValue
    global minValue
    if index == n - 1:
        if maxValue < result:
            maxValue = result
        if minValue > result:
            minValue = result
        return

    for i in range(4):
        if opList[i] > 0:
            opList[i] -= 1
            if i == 0:
                temp = result + numList[index + 1]
            elif i == 1:
                temp = result - numList[index + 1]
            elif i == 2:
                temp = result * numList[index + 1]
            else:
                temp = int(result / numList[index + 1])
            dfs(index + 1, temp)
            opList[i] += 1


for test_case in range(1, T + 1):
    n = int(input())
    opList = list(map(int, input().split()))
    numList = list(map(int, input().split()))
    maxValue = -9999999999
    minValue = 9999999999
    dfs(0, numList[0])
    print("#{} {}".format(test_case, maxValue - minValue))
