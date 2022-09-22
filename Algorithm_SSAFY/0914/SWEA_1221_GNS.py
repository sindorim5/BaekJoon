import sys

sys.stdin = open("./0914/GNS.txt", "r", encoding="UTF-8")
# sys.stdin = open("input.txt", "r", encoding="UTF-8")


T = int(input())


for test_case in range(1, T+1):
    tc, n = input().split()
    n = int(n)

    inputList = list(input().split())

    strDict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0,
               "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    result = []
    for element in inputList:
        strDict[element] += 1

    print(tc)
    for key, value in strDict.items():
        for _ in range(value):
            result.append(key)
    print(" ".join(result))
