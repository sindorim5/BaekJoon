import sys

sys.stdin = open("0908/최적경로.txt", "r", encoding="UTF-8")

T = int(input())

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dfs(depth, departure, nowDistance):
    global minValue
    if nowDistance > minValue:
        return
    if depth == n:
        nowDistance += distance(departure, end)
        if minValue > nowDistance:
            minValue = nowDistance
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, customer[i], nowDistance + distance(departure, customer[i]))
            visited[i] = False


for test_case in range(1, T+1):
    n = int(input())
    locations = list(map(int, input().split()))
    visited = [False for _ in range(n)]
    start = [locations[0], locations[1]]
    end = [locations[2], locations[3]]
    customer = []
    for i in range(4,len(locations),2):
        customer.append([locations[i], locations[i+1]])

    minValue = 999999999
    dfs(0, start, 0)
    print("#{} {}".format(test_case, minValue))
