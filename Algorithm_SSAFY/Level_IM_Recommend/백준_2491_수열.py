import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

n = int(input())
arr = list(map(int, input().split()))


def checkNum(arr):
    count = 1
    maxValue = 1
    for i in range(1, len(arr)):
        if arr[i - 1] <= arr[i]:
            count += 1
        else:
            count = 1

        if maxValue < count:
            maxValue = count
    return maxValue


a = checkNum(arr)
b = checkNum(arr[::-1])

print(max(a, b))
