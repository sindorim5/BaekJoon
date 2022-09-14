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

for c in candidate:
    print(c)
print("*************************")

def check(road):
    used = [False for _ in range(N)]
    i = 0
    while i < N-1:
        if road[i] - road[i + 1] == 1:
            delta = 1
            while delta <= L:
                if 0 <= i + delta < N:
                    if road[i] - road[i + delta] == 1:
                        used[i+delta] = True
                    else:
                        return 0
                else:
                    return 0
                delta += 1
        elif road[i] - road[i + 1] == -1:
            delta = 0
            while abs(delta) < L:
                if 0 <= i + delta < N:
                    if road[i + 1] - road[i + delta] == -1:
                        used[i + delta] = True
                    else:
                        return 0
                else:
                    return 0
                delta -= 1
        i += 1
    return 1

for road in candidate:
    count += check(road)

print(count)