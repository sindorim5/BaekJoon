from collections import deque


def solution(s):
    q = deque()

    if s[0] == ')':
        return False

    for c in s:
        if not q:
            if c == '(':
                q.append(c)
            else:
                return False
        else:
            if c == '(':
                q.append(c)
            else:
                q.pop()

    answer = False
    if not q:
        answer = True

    return answer
