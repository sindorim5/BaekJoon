def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1234567

"""
너무 많은 재귀호출로 런타임에러, 시간 초과
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

def solution(n):
    answer = fibo(n) % 1234567
    return answer
"""
