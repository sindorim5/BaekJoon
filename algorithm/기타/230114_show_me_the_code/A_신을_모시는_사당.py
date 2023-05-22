import sys

sys.stdin = open('input.txt', 'r', encoding='UTF-8')

n = int(input())

dollList = list(map(int, input().split()))


def color(start, count):
    left, right = 0, 0
    for i in range(count):
        if dollList[start+i] == 1:
            left += 1
        else:
            right += 1

    return abs(left - right)


answer = 1
for i in range(2, n+1):
    for j in range(n-i+1):
        answer = max(answer, color(j, i))

print(answer)
