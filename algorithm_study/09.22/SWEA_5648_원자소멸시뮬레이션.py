import sys
from collections import deque

sys.stdin = open("09.22/원자소멸시뮬레이션.txt", "r", encoding="UTF-8")

# 상 하 좌 우
direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
matrix = [[0] * 4001 for _ in range(4001)]
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # -1000 ~ 1000을 0.5 단위 고려해서 0 ~ 4000까지. 에너지는 배열.
    atoms = deque()  # x, y, 방향, 에너지
    for i in range(N):
        data = list(map(int, input().split()))
        # 입력 받은 데이터를 0 ~ 4000 좌표계에 맞게 수정
        data[0] = (data[0] + 1000) * 2
        data[1] = (data[1] + 1000) * 2
        matrix[data[1]][data[0]] = data[3]
        atoms.append(data)

    result = 0
    while len(atoms) != 0:
        number = len(atoms)
        for _ in range(number):
            q = atoms.popleft()
            nowX, nowY, d, e = q[0], q[1], q[2], q[3]
            nX, nY = nowX + direction[d][1], nowY + direction[d][0]
            if 0 <= nY < 4001 and 0 <= nX < 4001:
                # 충돌이 없었으면 에너지는 같은 값이어야 한다.
                if e == matrix[nowY][nowX]:
                    # 아무도 방문하지 않은 곳이면
                    if matrix[nY][nX] == 0:
                        matrix[nowY][nowX] = 0  # 이전 위치 초기화
                        # 이동
                        q[0], q[1] = nX, nY
                        matrix[nY][nX] = e
                        atoms.append(q)  # 다시 리스트에 집어 넣기
                    # 이미 다른 원자가 방문한 곳이면
                    else:
                        matrix[nY][nX] += e
                        # 해당 위치에 자신의 원자 에너지 더해주고
                        matrix[nowY][nowX] = 0  # 이전 위치 초기화
                # 충돌이 일어난 경우
                else:
                    result += matrix[nowY][nowX]  # power에 충돌한 에너지 총합 더해주고
                    matrix[nowY][nowX] = 0  # 현재 위치 초기화
            # 범위를 넘어가는 경우 값을 버린다.
            else:
                matrix[nowY][nowX] = 0  # 현재 위치 초기화

    print("#{} {}".format(test_case, result))
