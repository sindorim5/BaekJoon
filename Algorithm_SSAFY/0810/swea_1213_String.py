import sys

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0810/input_1213.txt", "r", encoding='utf-8')

T = 10

for _ in range(1, T+1):
    n = int(input())
    target = input()
    targetLen = len(target)
    line = input()
    count = 0
    i = 0
    j = 0
    while i <= len(line) - len(target):
        if line[i] == target[0]:
            temp = line[i:i+targetLen]
            if temp == target:
                count += 1
                i += targetLen
        i += 1

    print("#{} {}".format(n, count))
