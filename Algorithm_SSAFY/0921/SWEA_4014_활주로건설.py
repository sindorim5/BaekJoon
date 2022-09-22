import sys

sys.stdin = open("0921/활주로.txt", "r", encoding="UTF-8")

T = int(input())

def check(road):
    used = [False for _ in range(n)]
    for i in range(n-1):
        if road[i] == road[i+1]:
            continue
        # 내려갈 때
        elif road[i] - road[i+1] == 1:
            if not used[i+1]:
                delta = 2
                while delta <= m:
                    nX = i + delta
                    if 0 <= nX < n:
                        if road[i+1] == road[i+delta] and not used[i+delta]:
                            delta += 1
                            continue
                        else:
                            return 0
                    else:
                        return 0
            else:
                return 0
            for idx in range(1, m+1):
                used[i+idx] = True
        # 올라갈 때
        elif road[i] - road[i+1] == -1:
            if not used[i]:
                delta = 1
                while delta < m:
                    nX = i - delta
                    if 0 <= nX < n:
                        if road[i] == road[i-delta] and not used[i-delta]:
                            delta += 1
                            continue
                        else:
                            return 0
                    else:
                        return 0
            else:
                return 0
            for idx in range(m):
                used[i-idx] = True
        # 높이 차이가 1 초과
        else:
            return 0
    return 1



for test_case in range(1, T+1):
    n, m = map(int, input().split())
    roads = []
    matrix = []
    result = 0
    for _ in range(n):
        temp = list(map(int, input().split()))
        matrix.append(temp)
        roads.append(temp)
    
    for x in range(n):
        temp = []
        for y in range(n):
            temp.append(matrix[y][x])
        roads.append(temp)

    for road in roads:
        result += check(road)
    
    print("#{} {}".format(test_case, result))