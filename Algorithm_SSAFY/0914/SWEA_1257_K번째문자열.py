import sys

sys.stdin = open("./0914/K번째문자열.txt", "r", encoding="UTF-8")

T = int(input())

for test_case in range(1, T+1):
    k = int(input())
    inputStr = (input())
    inputLen = len(inputStr)
    alphaList = list(set(inputStr))
    alphaList.sort()
    indexList = []
    result = []
    
    for alpha in alphaList:
        tempIndex = []
        for i in range(inputLen):
            if inputStr[i] == alpha:
                tempIndex.append(i)
        indexList.append(tempIndex)

    for tempList in indexList:
        temp = []
        for index in tempList:
            for i in range(1, inputLen+1):
                if index+i >= inputLen+1:
                    break
                tempWord = "".join(inputStr[index:index+i])
                if tempWord not in temp:
                    temp.append(tempWord)
        temp.sort()
        result += temp

        if len(result) >= k:
            break
    
    if len(result) >= k:
        print("#{} {}".format(test_case, result[k-1]))
    else:
        print("#{} none".format(test_case))
    