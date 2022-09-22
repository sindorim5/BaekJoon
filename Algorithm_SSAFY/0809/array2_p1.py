import sys

sys.stdin = open("C:/SSAFY/clone/Algorithm_SSAFY/0810/input2_p1.txt", "r")

matrix = [list(map(int, input().split())) for _ in range(5)]

sum = 0

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for y in range(5):
    for x in range(5):
        for case in (0, 1, 2, 3):
            temp = 0
            nY = y + dy[case]
            nX = x + dx[case]
            if nY >= 5 or nY < 0 or nX >= 5 or nX < 0:
                temp = 0
            else:
                temp = abs(matrix[nY][nX] - matrix[y][x])
            sum += temp

print(sum)
