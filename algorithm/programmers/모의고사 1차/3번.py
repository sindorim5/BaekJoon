from collections import deque


def solution(order):
    index = 0
    q = deque()
    subQ = deque()
    for i in range(1, len(order) + 1):
        q.append(i)

    while q:
        if order[index] != q[0]:
            if subQ and subQ[-1] == order[index]:
                subQ.pop()
                index += 1
            else:
                subQ.append(q.popleft())
        else:
            q.popleft()
            index += 1

    while subQ:
        if order[index] == subQ[-1]:
            subQ.pop()
            index += 1
        else:
            break
    return index
