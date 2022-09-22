import sys
sys.stdin = open("0921/무선충전.txt", "r", encoding="UTF-8")

T = int(input())

dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]


def pickOne(aList, bList):
    result = -99999
    aValue, bValue = 0, 0
    for i in aList:
        for j in bList:
            if i == -1 and j == -1:
                aValue, bValue = 0, 0
                result = max(result, aValue + bValue)
            elif i != -1 and j != -1 and i == j:
                result = max(result, chargers[i][3])
            elif i == -1 and j != -1:
                aValue = 0
                bValue = chargers[j][3]
                result = max(result, aValue + bValue)
            elif i != -1 and j == -1:
                aValue = chargers[i][3]
                bValue = 0
                result = max(result, aValue + bValue)
            else:
                aValue = chargers[i][3]
                bValue = chargers[j][3]
                result = max(result, aValue + bValue)
    return result

for test_case in range(1, T+1):
    M, A = map(int, input().split())
    aMove = list(map(int, input().split()))
    bMove = list(map(int, input().split()))
    chargers = []
    aCord = []
    bCord = []
    for idx in range(A):
        x, y, c, p = map(int,input().split())
        chargers.append([y-1, x-1, c, p])

    result = 0
    # A와 B의 이동경로
    aNow = [0, 0]
    bNow = [9, 9]
    aCord.append(aNow)
    bCord.append(bNow)
    for i in range(M):
        deltaA = aMove[i]
        deltaB = bMove[i]
        yA, xA = aCord[-1]
        yB, xB = bCord[-1]
        aCandidate, bCandidate = [], []
        # 현재 위치에서 닿을 수 있는 충전소를 저장
        for j in range(A):
            charger = chargers[j]
            if abs(yA - charger[0]) + abs(xA - charger[1]) <= charger[2]:
                aCandidate.append(j)
            if abs(yB - charger[0]) + abs(xB - charger[1]) <= charger[2]:
                bCandidate.append(j)
        # 없다면 기록용으로 -1을 저장
        if len(aCandidate) == 0:
            aCandidate.append(-1)
        if len(bCandidate) == 0:
            bCandidate.append(-1)

        # 충전하기
        result += pickOne(aCandidate, bCandidate)

        # 다음 위치로 이동
        yA += dy[deltaA]
        xA += dx[deltaA]
        yB += dy[deltaB]
        xB += dx[deltaB]
        
        aCord.append([yA, xA])
        bCord.append([yB, xB])
    
    # 마지막 위치에 대한 충전소 계산
    aCandidate, bCandidate = [], []
    for j in range(A):
        charger = chargers[j]
        if abs(aCord[-1][0] - charger[0]) + abs(aCord[-1][1] - charger[1]) <= charger[2]:
            aCandidate.append(j)
        if abs(bCord[-1][0] - charger[0]) + abs(bCord[-1][1] - charger[1]) <= charger[2]:
            bCandidate.append(j)
    if len(aCandidate) == 0:
        aCandidate.append(-1)
    if len(bCandidate) == 0:
        bCandidate.append(-1)
    result += pickOne(aCandidate, bCandidate)

    print("#{} {}".format(test_case, result))