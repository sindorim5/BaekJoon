def solution(brown, yellow):
    answer = []

    a = brown + yellow      # a = x * y
    b = (brown + 4) // 2    # b = x + y
    for x in range(a, 0, -1):
        if a % x == 0:
            y = a // x
            if x + y == b:
                answer = [x, y]
                break
    return answer


"""
x: 가로, y: 세로
brown + yellow = x * y
yellow = (x-2) * (y-2)
식 정리를 하면 (brown + 4) / 2 = x + y
조건의 맞는 수를 for문을 돌면서 찾기

"""
