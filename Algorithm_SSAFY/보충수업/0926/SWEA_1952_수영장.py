import sys

sys.stdin = open("수영장.txt", "r", encoding="UTF-8")

T = int(input())

for test_case in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    plans = list(map(int, input().split()))
    DP = [0 for _ in range(13)]

    for idx in range(1, 13):
        dayPlan = day * plans[idx-1]

        DP[idx] = DP[idx-1] + min(dayPlan, month)

        if idx >= 2:
            temp = DP[idx-3] + three_month
            DP[idx] = min(DP[idx], temp)

    DP[12] = min(DP[12], year)

    print("#{} {}".format(test_case, DP[12]))
