def solution(s):
    arr = list(map(int, s.split()))
    answer = "{} {}".format(min(arr), max(arr))
    return answer
