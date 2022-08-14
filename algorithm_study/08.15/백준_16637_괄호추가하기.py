n = int(input())

arr = list(map(int, input().split()))


def calculate(a, b, operator):
    if operator == "+":
        return int(a) + int(b)
    elif operator == "-":
        return int(a) - int(b)
    return int(a) * int(b)
