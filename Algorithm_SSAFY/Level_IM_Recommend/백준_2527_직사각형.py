import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")
input = sys.stdin.readline

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    xMin = max(x1, x2)
    xMax = min(p1, p2)
    yMin = max(y1, y2)
    yMax = min(q1, q2)

    xDiff = xMax - xMin
    yDiff = yMax - yMin

    if xDiff > 0 and yDiff > 0:
        print("a")
    elif xDiff == 0 and yDiff == 0:
        print("c")
    elif xDiff < 0 or yDiff < 0:
        print("d")
    else:
        print("b")
