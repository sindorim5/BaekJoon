def solution(s):
    answer = []
    count, zero = 0, 0
    while s != '1':
        one = 0

        # 0을 제거하고 1의 수 세기
        for c in s:
            if c == '1':
                one += 1
            else:
                zero += 1

        s = bin(one)
        s = s[2:]

        count += 1

    answer = [count, zero]
    return answer
