import sys

sys.stdin = open("hunter.txt", "r", encoding="UTF-8")

# 헌터가 이동하는 함수


def hunt(x, y, dist):
    global next, answer

    if dist >= answer:
        return

    if not next:
        answer = min(answer, dist)
        return

    # 다음으로 이동할 지점들로 이동하며 거리 계산
    temp = next[:]
    for num, nx, ny in temp:
        d = abs(x-nx) + abs(y-ny)

        next.remove((num, nx, ny))

        # 몬스터일 경우, 고객을 다음에 이동할 수 있는 위치로 추가
        if num > 0:
            i, j = customer[num]
            next.append((-num, i, j))

        hunt(nx, ny, dist + d)

        next.append((num, nx, ny))

        if num > 0:
            next.remove((-num, i, j))


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    monster = []
    customer = {}

    for i in range(N):
        row = list(map(int, input().split()))

        for j in range(N):
            if row[j] > 0:
                # 몬스터 번호, 행, 열
                monster.append((row[j], i, j))
            elif row[j] < 0:
                customer[-row[j]] = (i, j)

    # 다음으로 이동할 지점
    next = monster
    answer = float("inf")

    hunt(0, 0, 0)

    print("#{} {}".format(test_case, answer))
