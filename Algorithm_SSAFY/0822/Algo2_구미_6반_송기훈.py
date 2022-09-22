T = int(input())

# 대각선 합 구하기
def getXSum(y, x):
    sumValue = 0
    # 우하단 값
    nY = y + 1
    nX = x + 1
    while 0 <= nY < N and 0 <= nX < N:
        sumValue += matrix[nY][nX]
        nY += 1
        nX += 1

    # 우상단 값
    nY = y - 1
    nX = x + 1
    while 0 <= nY < N and 0 <= nX < N:
        sumValue += matrix[nY][nX]
        nY -= 1
        nX += 1

    # 좌하단 값
    nY = y + 1
    nX = x - 1
    while 0 <= nY < N and 0 <= nX < N:
        sumValue += matrix[nY][nX]
        nY += 1
        nX -= 1

    # 좌상단 값
    nY = y - 1
    nX = x - 1
    while 0 <= nY < N and 0 <= nX < N:
        sumValue += matrix[nY][nX]
        nY -= 1
        nX -= 1

    # 자기 자신 더하기
    sumValue += matrix[y][x]

    return sumValue


# 십자 합 구하기
def getCrossSum(y, x):
    sumValue = 0
    # column 값 더하기
    for i in range(N):
        sumValue += matrix[i][x]
    # row 값 더하기
    for j in range(N):
        sumValue += matrix[y][j]

    # column과 row에 자기 자신이 중복되므로 한번 빼주기
    sumValue -= matrix[y][x]

    return sumValue


for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    maxValue = 0

    for y in range(N):
        for x in range(N):
            maxValue = max(maxValue, getXSum(y, x), getCrossSum(y, x))

    print("#{} {}".format(test_case, maxValue))
