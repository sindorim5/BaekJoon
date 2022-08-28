import sys

sys.stdin = open("fish.txt", "r", encoding="UTF-8")

T = int(input())


def entrance_gate(num, angler, r):
    global N
    # ret: 모든 낚시꾼 총 이동 거리
    # ret2: 마지막 낚시꾼이 왼쪽에 입장하고 동일한 거리의 오른쪽에 입장 가능한 경우
    # 위치 반환을 위한 변수
    # dist: 게이트에서 떨어진 정도
    # flag: 좌우로 체크할 변수
    ret = 0
    ret2 = False
    dist = 0
    flag = -1
    while angler:
        x = num + (dist * flag)
        # 이동하고자 하는 좌표의 x가 낚시터 범위 내이면서 먼저 온 낚시꾼이 없는 경우,
        # 게이트 위치 번호로 어느 게이트로 들어온 낚시꾼인지 확인할 수 있게 표시
        if 0 <= x < N and fishing[x] == 0:
            fishing[x] += r
            ret += dist + 1
            angler -= 1
        # 같은 거리만큼 떨어진 오른쪽 확인하기 위해 flag *= -1
        flag *= -1

        # 왼쪽 먼저 검사 후, 오른쪽을 검사하고 다시 왼쪽을 검사한 경우는 다음칸을 봐야하기 때문에 cnt += 1
        if flag < 0 and angler != 0:
            dist += 1

        # 마지막 사람이 왼쪽에 들어간 경우, 오른쪽에 들어갈 수 있는 경우가 있는지 체크 후 해당 위치 반환
        if flag > 0 and angler == 0:
            x2 = num + (dist * flag)
            # 위 조건을 만족해 오른쪽에 입장한 경우도 체크해야하는 경우
            if 0 <= x2 < N and fishing[x2] == 0:
                # x는 기존에 왼쪽에 채워진 마지막 낚시꾼 위치, x2는 확인해보아야할 오른쪽 낚시꾼 위치
                ret2 = [x, x2]
    return ret, ret2


def dfs(depth, total):
    global result
    if depth == 3:
        if total < result:
            result = total
    result

    for i in range(3):
        if used[i]:
            continue
        used[i] = 1
        ret, ret2 = entrance_gate(graph[i][0], graph[i][1], i + 1)
        dfs(depth + 1, total + ret)

        # 마지막 낚시꾼이 좌측 입장 & 오른쪽 같은 거리에 빈자리가 있어 확인해야 하는 경우
        if ret2:
            fishing[ret2[0]] = 0
            fishing[ret2[1]] = i+1
            dfs(depth + 1, total + ret)
        # fishing 배열의 해당 낚시꾼 입장 초기화
        for j in range(N):
            if fishing[j] == i + 1:
                fishing[j] = 0
        used[i] = 0
    return


for test_case in range(1, T+1):
    N = int(input())
    fishing = [0] * N
    graph = []
    result = float('inf')
    used = [0] * 3

    for i in range(3):
        gate, cnt = map(int, input().split())
        graph.append([gate-1, cnt])
    dfs(0, 0)
    print("#{} {}".format(test_case, result))
