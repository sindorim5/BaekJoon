import sys

sys.stdin = open("./0907/균형점.txt", "r", encoding="UTF-8")
T = int(input())



for test_case in range(1, T+1):
    n = int(input())
    inputList = list(map(int, input().split()))
    locations = []
    answers = []
    for i in range(len(inputList)//2):
        locations.append([float(inputList[i]), float(inputList[len(inputList)//2 + i])])
    for i in range(len(locations) - 1):
        half = (locations[i][0] + locations[i+1][0]) / 2
        x = half
        leftX = locations[i][0]
        rightX = locations[i+1][0]
        left = locations[:i+1]
        right = locations[i+1:]
        while True:
            leftValue = 0
            rightValue = 0
            for i in range(len(left)):
                leftValue += left[i][1] / ((left[i][0] - x) * (left[i][0] - x))
            for i in range(len(right)):
                rightValue += right[i][1] / ((right[i][0] - x) * (right[i][0] - x))
            leftValue = round(leftValue, 13)
            rightValue = round(rightValue, 13)

            # 수렴하면 종료, 반올림 했으므로 오차는 맞게 되어있다.
            if x == leftX or x == rightX:
                break
            if rightValue == leftValue:
                break

            if leftValue > rightValue:
                leftX = x
                x = (rightX + leftX) / 2
            elif rightValue > leftValue:
                rightX = x
                x = (leftX + rightX) / 2
        
        answers.append(x)

    print("#{}".format(test_case), end=" ")
    for answer in answers:
        print("{:.10f}".format(answer), end=" ")
    print()