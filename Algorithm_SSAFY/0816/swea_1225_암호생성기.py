import sys

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0816/input_1225.txt", "r", encoding='utf-8')

T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    i = 1
    while True:
        num = arr.pop(0)
        num -= i

        if num <= 0:
            num = 0
            arr.append(num)
            break
        else:
            arr.append(num)

        i += 1
        if i >= 6:
            i = 1

    print("#{}".format(test_case), end=" ")
    for i in arr:
        print(i, end=" ")
    print()
