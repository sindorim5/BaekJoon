import sys

sys.stdin = open("0920/홈방범서비스.txt", "r", encoding="UTF-8")

T = int(input())

kList = [k * k + (k-1) * (k-1) for k in range(22)]

for test_case in range(1, T+1):
    n, m = map(int,input().split())
    matrix = []
    homeList = []
    maxValue = -999999999
    for y in range(n):
        temp = list(map(int, input().split()))
        for x in range(n):
            if temp[x] == 1:
                homeList.append((y,x))
        matrix.append(temp)
    
    for k in range(1, n+2):
        for y in range(n):
            for x in range(n):
                count = 0
                for home in homeList:
                    if abs(y-home[0]) + abs(x-home[1]) < k:
                        count += 1
                if count * m >= kList[k]:
                    maxValue = max(maxValue, count)

    print("#{} {}".format(test_case, maxValue))
