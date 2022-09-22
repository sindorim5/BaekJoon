import sys
from collections import deque

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0812/input_1219.txt", "r", encoding='utf-8')

T = 10
for test_case in range(1, T+1):
    n, pair = map(int, input().split())
    node = list(map(int, input().split()))

    arr = [[] for _ in range(100)]

    i = 0
    q = deque()
    while i < pair * 2:
        start = int(node[i])
        end = int(node[i + 1])
        arr[end].append(start)
        i += 2

    def bfs(n):
        i = 0
        q.append(n)
        while q:
            e = q.popleft()
            if 0 in arr[e]:
                i += 1
                continue
            for a in arr[e]:
                q.append(a)
        return i

    result = bfs(99)

    if result > 0:
        result = 1
    else:
        result = 0

    print("#{} {}".format(test_case, result))
