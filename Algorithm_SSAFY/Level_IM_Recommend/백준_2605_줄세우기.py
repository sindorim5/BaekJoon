import sys

sys.stdin = open("./input.txt", "r", encoding="utf-8")

n = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(n):
    result.insert(arr[i], i+1)

result = result[::-1]

for r in result:
    print(r, end=" ")
