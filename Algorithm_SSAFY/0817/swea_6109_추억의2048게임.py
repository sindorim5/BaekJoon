import sys
from collections import deque
sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0817/6109_input.txt", "r", encoding="utf-8")

T = int(input())

for test_case in range(1, T+1):
    n, direction = map(str, input().split())

    n = int(n)

    matrix = [list(map(int, input().split()))
              for _ in range(n)]

    if direction == "up":
        for x in range(n):
            tempQ = deque()
            inputList = []
            for y in range(n):
                if matrix[y][x] == 0:
                    continue
                elif not tempQ:
                    tempQ.append(matrix[y][x])
                    inputList.append(matrix[y][x])
                elif tempQ[-1] == matrix[y][x]:
                    inputList[-1] = tempQ[-1] * 2
                    tempQ.clear()
                else:
                    tempQ.append(matrix[y][x])
                    inputList.append(matrix[y][x])
            while len(inputList) < n:
                inputList.append(0)
            for j in range(n):
                matrix[j][x] = inputList[j]

    elif direction == "down":
        for x in range(n):
            tempQ = deque()
            inputList = []
            for y in range(n-1, -1, -1):
                if matrix[y][x] == 0:
                    continue
                elif not tempQ:
                    tempQ.append(matrix[y][x])
                    inputList.append(matrix[y][x])
                elif tempQ[-1] == matrix[y][x]:
                    inputList[-1] = tempQ[-1] * 2
                    tempQ.clear()
                else:
                    tempQ.append(matrix[y][x])
                    inputList.append(matrix[y][x])
            while len(inputList) < n:
                inputList.append(0)
            for j in range(n-1, -1, -1):
                matrix[j][x] = inputList[n-j-1]

    elif direction == "right":
        for y in range(n):
            tempQ = deque()
            inputList = []
            for x in range(n-1, -1, -1):
                if matrix[y][x] == 0:
                    continue
                elif not tempQ:
                    tempQ.append(matrix[y][x])
                    inputList.append(matrix[y][x])
                elif tempQ[-1] == matrix[y][x]:
                    inputList[-1] = tempQ[-1] * 2
                    tempQ.clear()
                else:
                    tempQ.append(matrix[y][x])
                    inputList.append(matrix[y][x])
                print(y, matrix[y][x])

            while len(inputList) < n:
                inputList.append(0)
            for i in range(n-1, -1, -1):
                matrix[y][i] = inputList[n-i-1]

    elif direction == "left":
        for y in range(n):
            tempQ = deque()
            inputList = []
            for x in range(n):
                if matrix[y][x] == 0:
                    continue
                elif not tempQ:
                    tempQ.append(matrix[y][x])
                    inputList.append(matrix[y][x])
                elif tempQ[-1] == matrix[y][x]:
                    inputList[-1] = tempQ[-1] * 2
                    tempQ.clear()
                else:
                    tempQ.append(matrix[y][x])
                    inputList.append(matrix[y][x])
            while len(inputList) < n:
                inputList.append(0)
            for i in range(n):
                matrix[y][i] = inputList[i]

    print("#{}".format(test_case))
    for m in matrix:
        print(" ".join(map(str, m)))
