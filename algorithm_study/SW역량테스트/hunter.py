import sys
from unittest import result

sys.stdin = open("hunter.txt", "r", encoding="UTF-8")

T = int(input())

# loc는 현재 위치(몬스터 1이면 loc == 1, )


def hunt(depth, loc, dist):
    global result, cnt
    if N == cnt:
        if result > dist:
            result = dist
        return
    # 현재 이동거리가 지금까지 최소 이동거리보다 커지면 return
    if dist > result:
        return

    for i in range(1, cnt+1):
        if used[i]:
            continue

        used[i] = 1
        # 현재 i가 몬스터라면 (i <= cnt //2 ) 클라이언트에 방문할 수 있도록
        # used 배열 0으로 초기화
        if i <= cnt // 2:
            used[i * (-1)] = 0
        hunt(depth + 1, i, dist + distance[loc][i])
        if i <= cnt // 2:
            used[i * (-1)] = 1
        used[i] = 0
    return


for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # cnt는 몬스터 + 클라이언트 저장
    cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c]:
                cnt += 1

    # 맨해튼 거리 구하기 위한 좌표저장
    # 각 포인트는 matrix에 저장된 값을 index로 가지는 위치에 좌표(x, y) 값이 저장됨
    # 몬스터의 index는 양수임으로 리스트의 앞쪽, 이와 대칭되는 클라이언트는 음수이므로 리스트의 뒤쪽부터 저장되며 각각이 매칭됨
    # [0 1 2 3 -3 -2 -1]
    # 0에는 사냥꾼의 위치 [0, 0]이 저장됨
    # points는 좌표 저장
    points = [[-1, -1] for _ in range(cnt + 1)]

    # 몬스터와 클라이언트 좌표 저장
    for r in range(N):
        for c in range(N):
            if matrix[r][c]:
                points[matrix[r][c]][0] = r
                points[matrix[r][c]][1] = c

    # 각 몬스터와 클라이언트 간의 맨해튼 거리를 저장할 배열 선언
    distance = [[0 for _ in range(cnt+1)] for _ in range(cnt+1)]

    # 각 몬스터와 클라이언트 간의 맨해튼 거리 저장
    for i in range(1, cnt):
        for j in range(i+1, cnt+1):
            distance[i][j] = abs(points[i][0] - points[j][0]) + \
                abs(points[i][1] - points[j][1])
            distance[j][i] = abs(points[i][0] - points[j][0]) + \
                abs(points[i][1] - points[j][1])

    # cnt // 2 기준으로 앞은 몬스터, 뒤는 클라이언트
    used = [1] + [0] * (cnt // 2) + [1] * (cnt // 2)

    # 처음 사냥꾼이 사냥을 할때는 몬스터만 방문하므로 범위는 1~cnt//2+1
    for i in range(1, cnt // 2 + 1):
        # 사냥꾼이 몬스터를 잡으러 가는 맨해튼 거리는 따로 구한다.
        res = points[i][0] + points[i][1]
        used[i * (-1)] = 0
        used[i] = 1
        hunt(1, i, res)
        used[i * (-1)] = 1
        used[i] = 0
