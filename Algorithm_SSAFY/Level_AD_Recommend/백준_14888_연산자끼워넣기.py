import sys

sys.stdin = open("input.txt", "r", encoding="UTF-8")

n = int(input())
aList = list(map(int, input().split()))
opList = list(map(int, input().split()))
maxValue = -10000000001
minValue = 1000000001


def dfs(idx, sumValue, plus, minus, multiply, divide):
    global maxValue, minValue
    if idx == n:
        if sumValue > maxValue:
            maxValue = sumValue
        if sumValue < minValue:
            minValue = sumValue
    if plus:
        sumValue += aList[idx]
        dfs(idx + 1, sumValue, plus - 1, minus, multiply, divide)
        sumValue -= aList[idx]
    if minus:
        sumValue -= aList[idx]
        dfs(idx + 1, sumValue, plus, minus - 1, multiply, divide)
        sumValue += aList[idx]
    if multiply:
        temp = sumValue
        sumValue *= aList[idx]
        dfs(idx + 1, sumValue, plus, minus, multiply - 1, divide)
        sumValue = temp
    if divide:
        temp = sumValue
        if sumValue < 0:
            sumValue = abs(sumValue) // aList[idx]
            sumValue *= -1
        else:
            sumValue = sumValue // aList[idx]
        dfs(idx + 1, sumValue, plus, minus, multiply, divide - 1)
        sumValue = temp


dfs(1, aList[0], opList[0], opList[1], opList[2], opList[3])

print(maxValue)
print(minValue)
