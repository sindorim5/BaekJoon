import sys

sys.stdin = open("./input.txt", "r", encoding="utf-8")

garo, sero = map(int, input().split())
n = int(input())

seroRange = [0, sero]
garoRange = [0, garo]

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        seroRange.append(b)
    else:
        garoRange.append(b)

seroRange.sort()
garoRange.sort()


def findMax(arr):
    maxValue = 0
    for i in range(len(arr) - 1):
        temp = arr[i + 1] - arr[i]
        maxValue = max(temp, maxValue)
    return maxValue


seroMax = findMax(seroRange)
garoMax = findMax(garoRange)

print(seroMax * garoMax)
