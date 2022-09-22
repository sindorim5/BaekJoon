import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

n = 5
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

bingo = []
for _ in range(n):
    temp = list(map(int, input().split()))
    bingo += temp


def checkBingo(v):
    mainCount = 0
    # 가로 체크
    for y in range(n):
        count = 0
        for x in range(n):
            if v[y][x] == True:
                count += 1
        if count == 5:
            mainCount += 1

    # 세로 체크
    for x in range(n):
        count = 0
        for y in range(n):
            if v[y][x] == True:
                count += 1
        if count == 5:
            mainCount += 1

    # 대각 체크
    count = 0
    for i in range(n):
        if v[i][i] == True:
            count += 1
    if count == 5:
        mainCount += 1

    # 대각 체크2
    count = 0
    for i in range(n):
        if v[i][n - i - 1]:
            count += 1
    if count == 5:
        mainCount += 1

    if mainCount >= 3:
        return True
    else:
        return False


def findNumber(num, m, v):
    for y in range(n):
        for x in range(n):
            if m[y][x] == num:
                v[y][x] = True
                return


for i in range(len(bingo)):
    findNumber(bingo[i], matrix, visited)

    if i >= 4:
        if checkBingo(visited):
            print(i + 1)
            exit()
