import sys

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0811/input_1217.txt", "r", encoding='utf-8')

T = 10
for test_case in range(1, T+1):
    n = int(input())
    num, power = map(int, input().split())

    def multiply(x, p):
        if p == 1:
            return x
        return x * multiply(x, p-1)

    print("#{} {}".format(n, multiply(num, power)))
