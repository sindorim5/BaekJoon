import sys

# sys.stdin = open("0906/암호코드스캔.txt", "r", encoding="UTF-8")
sys.stdin = open("input2.txt", "r", encoding="UTF-8")
T = int(input())

hex_to_bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100",
              "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001",
              "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

numberDict = {"3211": 0, "2221": 1, "2122": 2, "1411": 3, "1132": 4,
              "1231": 5, "1114": 6, "1312": 7, "1213": 8, "3112": 9}


def hexToBinary(arr):
    # 16진수 아래 있는 0의 연속들을 잘라내고 변환
    # 16진수 -> 2진수
    binaryCode = ""
    for v in arr:
        binaryCode += hex_to_bin[v]
    return binaryCode


def ratioCheck(arr, multi):
    ratio = []
    queue = []
    for i in range(len(arr)):
        if not queue:
            queue.append(arr[i])
        else:
            if queue[-1] == arr[i]:
                queue.append(arr[i])
            else:
                ratio.append(str(len(queue) // multi))
                queue = [arr[i]]
    if queue:
        ratio.append(str(len(queue) // multi))
    return "".join(ratio)


def decodeCheck(arr):
    a = (arr[0] + arr[2] + arr[4] + arr[6]) * 3
    b = arr[1] + arr[3] + arr[5] + arr[7]
    if (a + b) % 10 == 0:
        return sum(arr)
    else:
        return 0

def binaryGenerator(arr, multi):
    binaryArr = []
    binary = ""
    for temp in arr:
        temp = temp.rstrip("0")
        check = 0
        binary = ""
        for i in range(len(temp)-1, -1, -1):
            binary += temp[i]
            if temp[i] == "0":
                check += 1
            else:
                check = 0
            if check == 4:
                check = 0
                if len(binary) >= 56:
                    binaryArr.append(binary[::-1])
                binary = ""
        if len(binary) >= 56:
            binaryArr.append(binary[::-1])
    return binaryArr

for test_case in range(1, 2):
    n, m = map(int, input().split())
    # 메모리 초과 때문에 입력과 동시에 변환
    matrix = set(hexToBinary(input().strip()) for _ in range(n))
    matrix = sorted(list(matrix))
    matrix.pop(0)
    binaryArr = binaryGenerator(matrix)
    if n >= 56:
        multiply = n // 56
    else:
        multiply = 1
    tempResult = 0
    result = 0
    for binary in binaryArr:
        for multi in range(multiply, 0, -1):
            i = 0
            keep = 0
            flag = 0
            decoded = []
            indexList = []
            multi_7 = multi * 7
            while i <= len(binary) - multi_7:
                code = binary[i:i+multi_7]
                codeRatio = ratioCheck(code, multi)
                if codeRatio in numberDict:
                    decoded.append(numberDict[codeRatio])
                    if len(decoded) == 1:
                        keep = i + 1
                    i += multi_7
                else:
                    decoded = []
                    if keep == 0:
                        i += 1
                    else:
                        i = keep
                        keep = 0
                if len(decoded) == 8:
                    tempResult = decodeCheck(decoded)
                    if tempResult:
                        result += tempResult
                        flag = 1
                        break
            if flag == 1:
                break
    print("#{} {}".format(test_case, result))
