import sys

sys.stdin = open("./input.txt", "r", encoding="utf-8")

arr = [int(input()) for _ in range(9)]

sumValue = sum(arr)

for i in range(len(arr) - 1):
    for j in range(1, len(arr)):
        if sumValue - arr[i] - arr[j] == 100:
            a = arr[i]
            b = arr[j]
            arr.remove(a)
            arr.remove(b)
            arr.sort()
            for k in arr:
                print(k)
            exit()
