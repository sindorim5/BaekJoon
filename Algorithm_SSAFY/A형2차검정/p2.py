import sys

sys.stdin = open("sampleinput2.txt", "r", encoding="UTF-8")

T = int(input())


def buyStock(money, profitArr):
    countArr = []

    for profit in profitArr:
        count = money // profit[1]
        countArr.append(count)

    depth = sum(countArr)

    def dfs(nowDepth, cash, income, countArr):
        global maxValue
        if nowDepth == depth:
            maxValue = max(maxValue, income)
            return
        for i in range(len(countArr)):
            if countArr[i] > 0:
                if cash - profitArr[i][1] >= 0:
                    countArr[i] -= 1
                    dfs(nowDepth+1, cash - profitArr[i][1], income + profitArr[i][0], countArr)
                    countArr[i] += 1
                else:
                    maxValue = max(maxValue, income)

    dfs(0, money, 0, countArr)

    return


for test_case in range(1, T+1):
    original, monthly = map(int, input().split())
    stockNum, pastMonth = map(int, input().split())
    stocks = [list(map(int, input().split())) for _ in range(stockNum)]
    maxValue = -1
    totalOriginal = original + monthly * pastMonth

    for i in range(0, pastMonth):
        maxValue = -1
        if i != 0:
            original += monthly
        profit = []
        for j in range(stockNum):
            if stocks[j][i + 1] - stocks[j][i] > 0:
                profit.append([stocks[j][i + 1] - stocks[j][i], stocks[j][i]])

        buyStock(original, profit)
        if maxValue == -1:
            maxValue = 0
        original += maxValue
    original += monthly

    print("#{} {}".format(test_case, original-totalOriginal))