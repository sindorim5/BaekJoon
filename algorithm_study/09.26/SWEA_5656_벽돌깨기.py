import sys
import copy
from collections import deque
# sys.stdin = open("09.26/벽돌깨기.txt", "r", encoding="UTF-8")
sys.stdin = open("input.txt", "r", encoding="UTF-8")
# 하 좌 우
dy = [-1, 0, 0]
dx = [0, -1, 1]

T = int(input())

def drop(idx, arr):
    count = 0
    startY = -1
    for y in range(h):
        if arr[y][idx] > 0:
            startY = y
            count = arr[y][idx]
    if count > 0:
        # 하 좌 우 0으로 만들기
        q = deque()
        q.append([startY, idx, count])
        arr[startY][idx] = 0
        while q:
            nowY, nowX, popCount = q.popleft()
            for d in range(3):
                i = 0
                while i < popCount-1:
                    nY = nowY + dy[d]
                    nX = nowX + dx[d]
                    if 0 <= nY < h and 0 <= nX < w:
                        if arr[nY][nX] == 0:
                            continue
                        q.append([nY, nX, arr[nY][nX]])
                        arr[nY][nX] = 0
                    else:
                        break
                    i += 1
        # 0 정리하기
        for x in range(w):
            sortZero = []
            for y in range(h-1, -1, -1):
                if arr[y][x] > 0:
                    sortZero.append(arr[y][x])
                    arr[y][x] = 0
            for i in range(len(sortZero)):
                arr[h-1-i][x] = sortZero[i]
    for asdf in arr:
        print(arr)

def block(depth, arr):
    global minBlock
    if depth == n:
        count = 0
        for y in range(h):
            for x in range(w):
                if arr[y][x] > 0:
                    count += 1
        minBlock = min(minBlock, count)
        return
    tempArr = copy.deepcopy(arr)
    for x in range(w):
        block(depth, drop(x, tempArr))

for test_case in range(1, 2):
    n, w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]
    minBlock = 10**9
    block(0, matrix)

    print(minBlock)
