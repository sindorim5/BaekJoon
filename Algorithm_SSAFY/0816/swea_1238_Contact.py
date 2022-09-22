import sys
from collections import deque

sys.stdin = open(
    "E:/workspace/Java_Study/Algorithm_SSAFY/0816/input_1238.txt", "r", encoding="utf-8"
)

T = 10

for test_case in range(1, T + 1):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    childList = [set() for _ in range(101)]
    visited = [-1 for _ in range(101)]
    q = deque()
    callList = []
    for i in range(0, n, 2):
        childList[arr[i]].add(arr[i + 1])
    depth = 0
    q.append((depth, start))
    while q:
        nowDepth, now = q.popleft()
        for child in childList[now]:
            if visited[child] < 0:
                visited[child] = nowDepth + 1
                callList.append((nowDepth + 1, child))
                q.append((nowDepth + 1, child))

    callList.sort(key=lambda x: (x[0], x[1]))
    print("#{} {}".format(test_case, callList[-1][1]))
