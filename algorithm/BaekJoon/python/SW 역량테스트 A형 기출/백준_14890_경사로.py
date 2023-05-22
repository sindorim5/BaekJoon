import sys

sys.stdin = open("./input.txt", "r", encoding="UTF-8")

N, L = map(int, input().split())

matrix = []
candidate = []
count = 0

for y in range(N):
    temp = list(map(int, input().split()))
    matrix.append(temp)
    candidate.append(temp)

for x in range(N):
    temp = []
    for y in range(N):
        temp.append(matrix[y][x])
    candidate.append(temp)


def check(road):
    used = [False for _ in range(N)]
    i = 0
    for i in range(N-1):
        if road[i] == road[i+1]:
            continue
        elif abs(road[i] - road[i+1]) > 1:
            return 0
        elif road[i] > road[i+1]:
            temp = road[i+1]
            for j in range(i+1, i+L+1):
                # j가 맵 안에 있을 때
                if 0 <= j < N:
                    # 높이가 다를 때, 이미 건설 되었을 때
                    if temp != road[j]:
                        return 0
                    elif used[j]:
                        return 0
                    # 위의 경우가 아니면 건설
                    used[j] = True
                else:
                    return 0
        else:
            temp = road[i]
            for j in range(i, i-L, -1):
                if 0 <= j < N:
                    if temp != road[j]:
                        return 0
                    elif used[j]:
                        return 0
                    used[j] = True
                else:
                    return 0
    return 1


for road in candidate:
    count += check(road)

print(count)
