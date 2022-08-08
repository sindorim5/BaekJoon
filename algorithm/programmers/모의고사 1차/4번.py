import copy


def changeCol(matrix, x):
    for y in range(len(matrix)):
        if matrix[y][x] == 0:
            matrix[y][x] = 1
        else:
            matrix[y][x] = 0


def changeRow(matrix, y):
    for x in range(len(matrix[0])):
        if matrix[y][x] == 0:
            matrix[y][x] = 1
        else:
            matrix[y][x] = 0


def solution(beginning, target):
    answerArr = [0, 0, 0, 0]

    for i in range(2):
        flag = 0
        count = 0

        temp = copy.deepcopy(beginning)

        while temp != target:
            if flag == 0:
                # 왼쪽
                for y in range(len(beginning)):
                    if temp[y][0] != target[y][0]:
                        changeRow(temp, y)
                        answerArr[i] += 1
                flag = 1
            else:
                # 윗쪽
                for x in range(len(beginning[0])):
                    if temp[0][x] != target[0][x]:
                        changeCol(temp, x)
                        answerArr[i] += 1
                flag = 0
            count += 1
            if count > len(beginning[0]) * len(beginning):
                answerArr[i] = -1
                break

    for i in range(2, 4):
        flag = 0
        count = 0
        temp = copy.deepcopy(beginning)

        while temp != target:
            if flag == 0:
                # 오른쪽
                for y in range(len(beginning)):
                    if temp[y][len(beginning) - 1] != target[y][len(beginning) - 1]:
                        changeRow(temp, y)

                        answerArr[i] += 1
                flag = 1
            else:
                # 아래쪽
                for x in range(len(beginning[0])):
                    if temp[len(beginning) - 1][x] != target[len(beginning) - 1][x]:
                        changeCol(temp, x)
                        answerArr[i] += 1
                flag = 0
            count += 1
            if count > 20:
                answerArr[i] = -1
                break

    return min(answerArr)
