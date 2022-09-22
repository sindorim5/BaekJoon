import sys

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0812/input_1234.txt", "r", encoding='utf-8')

T = 10
for test_case in range(1, T+1):
    length, number = map(str, input().split())

    numbers = list(number)

    i = 0

    while i < len(numbers) - 1:
        if numbers[i] == numbers[i + 1]:
            numbers.pop(i)
            numbers.pop(i)
            i -= 1
        else:
            i += 1

        if i >= len(numbers) - 1:
            result = "".join(numbers)
            break

    print("#{} {}".format(test_case, result))
