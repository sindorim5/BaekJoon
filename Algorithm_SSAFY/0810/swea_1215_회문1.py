import sys

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0810/input_1215.txt", "r", encoding='utf-8')

T = 10

for test_case in range(1, T+1):
    n = 8
    targetLen = int(input())
    matrix = [list(input()) for _ in range(n)]
    count = 0

    # 가로 탐색
    for y in range(n):
        for x in range(n - targetLen + 1):
            temp = matrix[y][x:x+targetLen]
            if temp == temp[::-1]:
                count += 1

    # 세로 탐색
    for x in range(n):
        for y in range(n - targetLen + 1):
            temp = []
            for i in range(targetLen):
                temp.append(matrix[y+i][x])
            if temp == temp[::-1]:
                count += 1

    print("#{} {}".format(test_case, count))
