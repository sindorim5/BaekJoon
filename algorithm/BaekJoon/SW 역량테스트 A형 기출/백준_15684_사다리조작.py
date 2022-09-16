import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")

input = sys.stdin.readline

n, m, h = map(int, input().split())

numbers = [i for i in range(n+1)]
matrix = [[0 for _ in range(n+1)] for _ in range(h+1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1

def down(arr):
    cnt = 0
    for num in range(1, n+1):
        temp = num
        i = 1
        while i <= h:
            if arr[i][temp]:
                temp += 1
            elif arr[i][temp - 1]:
                temp -= 1
            i += 1
        if num == temp:
            cnt += 1
        else:
            break
    if cnt == n:
        return True
    else:
        return False

