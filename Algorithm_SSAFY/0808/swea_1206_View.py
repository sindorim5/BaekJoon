import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10

for test_case in range(1, T + 1):
    n = int(input())
    count = 0

    building = list(map(int, input().split()))

    for i in range(2, n - 2):
        left1 = building[i] - building[i - 1]
        left2 = building[i] - building[i - 2]
        right1 = building[i] - building[i + 1]
        right2 = building[i] - building[i + 2]

        if left1 > 0 and left2 > 0 and right1 > 0 and right2 > 0:
            count += min(left1, left2, right1, right2)

    print("#{} {}".format(test_case, count))
