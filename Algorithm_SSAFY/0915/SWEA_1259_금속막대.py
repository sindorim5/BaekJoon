import sys

sys.stdin = open("0915/금속막대.txt", "r", encoding="UTF-8")

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    inputList = list(map(int, input().split()))
    screwList = []
    for i in range(0, len(inputList), 2):
        screwList.append([inputList[i], inputList[i+1]])

    connection = [screwList.pop(0)]

    i = 0
    while screwList:
        # 연결의 앞쪽에 추가
        if screwList[i][1] == connection[0][0]:
            connection.insert(0, screwList.pop(i))
            i = 0
        # 연결의 뒷쪽에 추가
        elif screwList[i][0] == connection[-1][1]:
            connection.append(screwList.pop(i))
            i = 0
        else:
            i += 1

    print("#{}".format(test_case), end=" ")
    for screw in connection:
        for s in screw:
            print(s, end=" ")
    print()
