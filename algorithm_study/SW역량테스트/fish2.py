from itertools import permutations

# 왼쪽으로 자리잡는 함수


def left(entry, dist):
    global grid, cnt

    if entry - dist > 0 and not grid[entry - dist]:
        grid[entry - dist] = dist + 1
        cnt += 1

# 오른쪽으로 자리잡는 함수


def right(entry, dist):
    global grid, cnt

    if entry - dist <= N and not grid[entry - dist]:
        grid[entry - dist] = dist + 1
        cnt += 1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(3)]
    answer = float('inf')
    ways = [[left, right], [right, left]]

    # 어느 출입문을 먼저 열지 결정
    for turn in permutations(range(3), 3):
        # 왼쪽, 오른쪽 중 어떤 방향을 우선으로 할지 결정
        for way in range(2):
            def1, def2 = ways[way]

            # 낚시꾼 자리배치
            grid = [0 for _ in range(N+1)]

            for i in turn:
                entry, fisher = graph[i]

                # 출입구 위치가 비어있는지 파악
                if grid[entry]:
                    cnt = 0
                else:
                    grid[entry] = 1
                    cnt = 1

                # 낚시꾼들이 모두 자리를 잡을 때까지 반복
                dist = 1
                while cnt < fisher:
                    def1(entry, dist)
                    if cnt == fisher:
                        break
                    def2(entry, dist)
                    dist += 1
            answer = min(answer, sum(grid))
    print("#{} {}".format(test_case, answer))
