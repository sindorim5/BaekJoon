import sys

sys.stdin = open("0819/1952_input.txt", "r", encoding="utf-8")

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    # 1일 1달 3달 1년
    fee = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    pay = [0 for _ in range(13)]

    for month in range(1, 13):
        pay[month] = min(fee[0] * plan[month], fee[1]) + pay[month - 1]

        if month >= 3:
            pay[month] = min(pay[month - 3] + fee[2], pay[month])

    pay[12] = min(pay[12], fee[3])

    print("#{} {}".format(test_case, pay[12]))
