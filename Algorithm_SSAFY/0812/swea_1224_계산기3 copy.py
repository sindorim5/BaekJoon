import sys

sys.stdin = open(
    "/Users/song/code/SSAFY_CODES/Algorithm_SSAFY/0812/input_1224.txt",
    "r",
    encoding="utf-8",
)

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    arr = input()
    stack = []  # stack
    result = []  # 후위 표기법 list

    # 후위 표기법 만들기
    for c in arr:
        # 숫자면 후위표기법 list에 추가
        if "0" <= c <= "9":
            result.append(c)
        else:
            if c == "(":
                stack.append(c)
            elif c == "*" or c == "/":
                # 우선 순위가 낮은 연산자가 나올 때까지 pop
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    result.append(stack.pop())
                # 나왔으니 stack에 넣어줌
                stack.append(c)
            elif c == "+" or c == "-":
                # 우선 순위가 낮은 연산자가 나올 때까지 pop
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                # 나왔으니 stack에 넣어줌
                stack.append(c)
            # c가 ) 이면 ( 가 나올 때까지 pop
            elif c == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                # ( 버림
                stack.pop()
    # stack의 남은 연산자를 더해줌
    while stack:
        result.append(stack.pop())

    # 후위 표기법 계산
    calStack = []
    for c in result:
        # 숫자는 stack에 추가
        if "0" <= c <= "9":
            calStack.append(int(c))
        # 연산자면 stack 숫자 두 개 꺼내서 계산 후 stack에 추가
        else:
            a = calStack.pop()
            b = calStack.pop()
            if c == "+":
                calStack.append(a + b)
            elif c == "-":
                calStack.append(a - b)
            elif c == "*":
                calStack.append(a * b)
            elif c == "/":
                calStack.append(a // b)

    print("#{} {}".format(test_case, calStack[0]))
