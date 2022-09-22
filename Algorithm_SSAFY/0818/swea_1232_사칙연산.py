import sys

sys.stdin = open("1232_input.txt", "r", encoding="utf-8")

# 후위 순회
def order(i):
    global stack
    if tree[i]:
        order(left[i])
        order(right[i])
        if type(tree[i]) == int:
            stack += [tree[i]]
        else:
            a = stack.pop()
            b = stack.pop()
            if tree[i] == "+":
                stack += [b + a]
            elif tree[i] == "-":
                stack += [b - a]
            elif tree[i] == "*":
                stack += [b * a]
            elif tree[i] == "/":
                stack += [b / a]


T = 10

for tc in range(1, T + 1):
    n = int(input())
    tree = [0] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for _ in range(n):
        temp = input().split()
        if len(temp) == 4:
            tree[int(temp[0])] = temp[1]
            left[int(temp[0])] = int(temp[2])
            right[int(temp[0])] = int(temp[3])
        else:
            tree[int(temp[0])] = int(temp[1])
    stack = []
    order(1)
    print("#{} {}".format(tc, int(stack[0])))
