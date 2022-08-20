# distance = 12
# scope = [[7, 8], [4, 6], [11, 10]]
# times = [[2, 2], [2, 4], [3, 3]]

distance = 10
scope = [[3, 4], [5, 8]]
times = [[2, 5], [4, 3]]


def solution(distance, scope, times):
    answer = distance
    hwarang = [[] for _ in range(distance + 1)]
    for i in range(len(scope)):
        scope[i].sort()
        startScope = scope[i][0]
        endScope = scope[i][1]
        for j in range(startScope, endScope + 1):
            # 시간범위 넘어가면 0으로 초기화
            location = j % (times[i][0] + times[i][1])
            # location이 0이 되면 해당 시간 때는 휴식상태
            if location != 0:
                # 근무시간보다 작거나 같을 경우에는 근무상태
                if location - times[i][0] <= 0:
                    hwarang[j] = 1

    for i in range(1, len(hwarang)):
        if hwarang[i] == 1:
            answer = i
            break

    return answer


print(solution(distance, scope, times))
