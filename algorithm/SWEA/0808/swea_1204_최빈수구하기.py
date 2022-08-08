import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = [0] * (max(arr) + 1)
    for i in arr:
        count[i] += 1
    # print(count)
    result = []
    for (index, value) in enumerate(count):
        if max(count) == count[index]:
            result.append(index)
    print(f"#{N} {result[-1]}")
