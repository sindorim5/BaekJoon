import sys

# sys.stdin = open("09.22/원자소멸시뮬레이션.txt", "r", encoding="UTF-8")
sys.stdin = open("09.22/temp.txt", "r", encoding="UTF-8")

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    atoms = [True for _ in range(n)]
    crash = []
    crashSet = []
    times = []
    timeSet = []

    for i in range(n-1):
        for j in range(i+1, n):
            # x 좌표가 같고 방향이 반대인 경우
            if matrix[i][0] == matrix[j][0]:
                if matrix[i][1] > matrix[j][1] and matrix[i][2] == 1 and matrix[j][2] == 0:
                    time = abs(matrix[i][1] - matrix[j][1]) / 2
                    crash.append([time, [matrix[i][0], matrix[j][1]+time], [i, j]])
                    times.append([time, [matrix[i][0], matrix[j][1]+time]])
                elif matrix[i][1] < matrix[j][1] and matrix[i][2] == 0 and matrix[j][2] == 1:
                    time = abs(matrix[i][1] - matrix[j][1]) / 2
                    crash.append([time, [matrix[i][0], matrix[j][1]-time], [i, j]])
                    times.append([time, [matrix[i][0], matrix[j][1]-time]])
            # y 좌표가 같고 방향이 반대인 경우
            elif matrix[i][1] == matrix[j][1]:
                if matrix[i][0] > matrix[j][0] and matrix[i][2] == 2 and matrix[j][2] == 3:
                    time = abs(matrix[i][0] - matrix[j][0]) / 2
                    crash.append([time, [matrix[i][0]-time, matrix[j][1]], [i, j]])
                    times.append([time, [matrix[i][0]-time, matrix[j][1]]])
                elif matrix[i][0] < matrix[j][0] and matrix[i][2] == 3 and matrix[j][2] == 2:
                    time = abs(matrix[i][0] - matrix[j][0]) / 2
                    crash.append([time, [matrix[i][0]+time, matrix[j][1]], [i, j]])
                    times.append([time, [matrix[i][0]+time, matrix[j][1]]])

            # i가 좌로 이동할 때
            if matrix[i][2] == 2:
                # j가 아래로 이동하고
                if matrix[j][2] == 1:
                    # i의 좌상단에 있다면 직각 이등변 삼각형 체크
                    if matrix[j][0] < matrix[i][0] and matrix[j][1] > matrix[i][1]:
                        xDiff = matrix[i][0] - matrix[j][0]
                        yDiff = matrix[j][1] - matrix[i][1]
                        if xDiff == yDiff:
                            crash.append([xDiff, [matrix[j][0], matrix[i][1]],[i, j]])
                            times.append([xDiff, [matrix[j][0], matrix[i][1]]])
                # j가 위로 이동하고
                elif matrix[j][2] == 0:
                    # i의 좌하단에 있다면 직각 이등변 삼각형 체크
                    if matrix[j][0] < matrix[i][0] and matrix[j][1] < matrix[i][1]:
                        xDiff = matrix[i][0] - matrix[j][0]
                        yDiff = matrix[i][1] - matrix[j][1]
                        if xDiff == yDiff:
                            crash.append([xDiff, [matrix[j][0], matrix[i][1]], [i, j]])
                            times.append([xDiff, [matrix[j][0], matrix[i][1]]])

            # i가 우로 이동할 때
            if matrix[i][2] == 3:
                # j가 아래로 이동하고
                if matrix[j][2] == 1:
                    # i의 우상단에 있다면 직각 이등변 삼각형 체크
                    if matrix[j][0] > matrix[i][0] and matrix[j][1] > matrix[i][1]:
                        xDiff = matrix[j][0] - matrix[i][0]
                        yDiff = matrix[j][1] - matrix[i][1]
                        if xDiff == yDiff:
                            crash.append([xDiff, [matrix[j][0], matrix[i][1]],[i, j]])
                            times.append([xDiff, [matrix[j][0], matrix[i][1]]])
                # j가 위로 이동하고
                elif matrix[j][2] == 0:
                    # i의 우하단에 있다면 직각 이등변 삼각형 체크
                    if matrix[j][0] > matrix[i][0] and matrix[j][1] < matrix[i][1]:
                        xDiff = matrix[j][0] - matrix[i][0]
                        yDiff = matrix[i][1] - matrix[j][1]
                        if xDiff == yDiff:
                            crash.append([xDiff, [matrix[j][0], matrix[i][1]], [i, j]])
                            times.append([xDiff, [matrix[j][0], matrix[i][1]]])

            # i가 위로 이동할 때
            if matrix[i][2] == 0:
                # j가 좌로 이동하고
                if matrix[j][2] == 2:
                    # i의 우상단에 있다면 직각 이등변 삼각형 체크
                    if matrix[j][0] > matrix[i][0] and matrix[j][1] > matrix[i][1]:
                        xDiff = matrix[j][0] - matrix[i][0]
                        yDiff = matrix[j][1] - matrix[i][1]
                        if xDiff == yDiff:
                            crash.append([xDiff, [matrix[i][0], matrix[j][1]], [i, j]])
                            times.append([xDiff, [matrix[i][0], matrix[j][1]]])
                # j가 우로 이동하고
                elif matrix[j][2] == 3:
                    # i의 좌상단에 있다면 직각 이등변 삼각형 체크
                    if matrix[j][0] > matrix[i][0] and matrix[j][1] < matrix[i][1]:
                        xDiff = matrix[j][0] - matrix[i][0]
                        yDiff = matrix[i][1] - matrix[j][1]
                        if xDiff == yDiff:
                            crash.append([xDiff, [matrix[i][0], matrix[j][1]], [i, j]])
                            times.append([xDiff, [matrix[i][0], matrix[j][1]]])
            
            # i가 아래로 이동할 때
            if matrix[i][2] == 1:
                # j가 좌로 이동하고
                if matrix[j][2] == 2:
                    # i의 우하단에 있다면 직각 이등변 삼각형 체크
                    if matrix[j][0] > matrix[i][0] and matrix[j][1] < matrix[i][1]:
                        xDiff = matrix[j][0] - matrix[i][0]
                        yDiff = matrix[i][1] - matrix[j][1]
                        if xDiff == yDiff:
                            crash.append([xDiff, [matrix[i][0], matrix[j][1]], [i, j]])
                            times.append([xDiff, [matrix[i][0], matrix[j][1]]])
                # j가 우로 이동하고
                elif matrix[j][2] == 3:
                    # i의 좌하단에 있다면 직각 이등변 삼각형 체크
                    if matrix[j][0] < matrix[i][0] and matrix[j][1] < matrix[i][1]:
                        xDiff = matrix[i][0] - matrix[j][0]
                        yDiff = matrix[i][1] - matrix[j][1]
                        if xDiff == yDiff:
                            crash.append([xDiff, [matrix[i][0], matrix[j][1]],[i, j]])
                            times.append([xDiff, [matrix[i][0], matrix[j][1]]])

    times.sort()
    crash.sort()
    # times 정리
    for element in times:
        if element not in timeSet:
            timeSet.append(element)
    # crash 정리
    i = 0
    for element in timeSet:
        time, cord = element[0], element[1]
        crashSet.append([time, set()])
        while crash[i][0] == time and crash[i][1] == cord:
            for idx in crash[i][2]:
                crashSet[-1][1].add(idx)
            i += 1
            if i == len(crash):
                break

    result = 0
    for element in crashSet:
        temp = list(element[1])
        candidate = []
        for i in temp:
            if atoms[i]:
                candidate.append(i)
        if len(candidate) > 1:
            for j in candidate:
                result += matrix[j][3]
                atoms[j] = False

    print("#{} {}".format(test_case, result))