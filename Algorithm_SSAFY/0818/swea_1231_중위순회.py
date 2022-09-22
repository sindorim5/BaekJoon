import sys

sys.stdin = open("1231_input.txt", "r", encoding="utf-8")

T = 10


def order(num):
    if num <= n:
        order(num * 2)
        print(letter[num], end="")
        order(num * 2 + 1)


for test_case in range(1, T + 10):
    n = int(input())
    letter = [0] * (n + 1)
    for i in range(n):
        inputList = list(input().split())
        letter[i + 1] = inputList[1]
    print("#{}".format(test_case), end=" ")
    order(1)
    print()
