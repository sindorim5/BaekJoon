import sys
from collections import deque

sys.stdin = open("input.txt", "r", encoding="utf-8")

for test_case in range(1, 3):
    text = input()
    q = deque()
    for t in text:
        if not q and t == ")":
            print("Invalid Input")
            break
        if t == "(":
            q.append(t)
        else:
            q.pop()
    if not q:
        print("#{} Valid Input".format(test_case))
    else:
        print("#{} Invalid Input".format(test_case))

# input
# ()()((()))
# ((()((((()()((()())((())))))
