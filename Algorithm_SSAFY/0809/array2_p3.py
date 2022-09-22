import sys

sys.stdin = open("C:/SSAFY/clone/Algorithm_SSAFY/0810/input2_p3.txt", "r")

y = 0
x = -1
n = 5
sign = 1
matrix = []
for _ in range(n):
    matrix += list(map(int, input().split()))

temp = [[0]*5 for _ in range(n)]


while n > 0:
    for i in range(n):
        x += sign
        num = min(matrix)
        matrix.remove(num)
        temp[y][x] = num
    n -= 1
    for j in range(n):
        y += sign
        num = min(matrix)
        matrix.remove(num)
        temp[y][x] = num
    sign *= -1

for i in temp:
    print(i)
