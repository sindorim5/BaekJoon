import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10

for test_case in range(1, T + 1):
    dumpCount = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    for _ in range(dumpCount):

        if (arr[-1] - arr[0]) <= 1:
            break
        else:
            arr[-1] -= 1
            arr[0] += 1
        arr.sort()

    dump = arr[-1] - arr[0]

    print("#{} {}".format(test_case, dump))
