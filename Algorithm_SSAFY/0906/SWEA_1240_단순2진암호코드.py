import sys

sys.stdin = open("0906/단순2진암호코드.txt", "r", encoding="UTF-8")

T = int(input())

numberDict = {"3211": 0, "2221": 1, "2122": 2, "1411": 3, "1132": 4,
              "1231": 5, "1114": 6, "1312": 7, "1213": 8, "3112": 9}


def ratioCheck(arr):    # 8자리 배열의 0, 1 비율 리턴
    ratio = []
    queue = []
    for i in range(len(arr)):
        if not queue:
            queue.append(arr[i])
        else:
            if queue[-1] == arr[i]:
                queue.append(arr[i])
            else:
                ratio.append(str(len(queue)))
                queue = [arr[i]]
    if queue:
        ratio.append(str(len(queue)))
    return "".join(ratio)


def decodeCheck(arr):   # 유효한 암호코드인지 확인하는 함수
    a = (arr[0] + arr[2] + arr[4] + arr[6]) * 3
    b = arr[1] + arr[3] + arr[5] + arr[7]
    if (a + b) % 10 == 0:
        return sum(arr)
    else:
        return 0


for test_case in range(1, T+1):
    n, m = map(int, input().split())
    matrix = set(input() for _ in range(n))
    matrix = sorted(list(matrix))
    matrix.pop(0)
    passcode = matrix[0]
    decoded = []
    i = 0
    keep = 0
    while i <= m - 7:
        code = passcode[i:i+7]
        codeRatio = ratioCheck(code)
        # 해독한 코드의 0,1 비율이 숫자에 대응될 때
        if codeRatio in numberDict:
            decoded.append(numberDict[codeRatio])
            # 8자리가 완성 안될 경우 다시 탐색을 시작할 인덱스 저장
            if len(decoded) == 1:
                keep = i + 1
            # 인덱스 7씩 늘려가며 탐색
            i += 7
        else:
            decoded = []
            # 저장된 인덱스가 없을 때 i는 다음 인덱스로
            if keep == 0:
                i += 1
            # 저장된 인덱스가 있을 때 i는 저장된 곳으로. keep은 0으로 초기화
            else:
                i = keep
                keep = 0
        # 8자리가 완성되면 탈출
        if len(decoded) == 8:
            break

    # while문을 통과하고 decoded 리스트가 존재하면
    if decoded:
        result = decodeCheck(decoded)
    # 그렇지 않으면 유효하지 않은 암호코드이므로 0
    else:
        result = 0

    print("#{} {}".format(test_case, result))
