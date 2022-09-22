import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")
input = sys.stdin.readline

k = int(input())
arr = []

for _ in range(6):
    direction, distance = map(int, input().split())
    arr.append(distance)

maxValue = 0
index = 0
for i in range(6):
    temp = arr[i] * arr[(i + 1) % 6]
    if maxValue < temp:
        maxValue = temp
        index = i

minValue = arr[(index + 3) % 6] * arr[(index + 4) % 6]

print(k * (maxValue - minValue))
