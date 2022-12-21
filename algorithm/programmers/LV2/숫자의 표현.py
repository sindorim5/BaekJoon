def solution(n):
    answer = 0
    for i in range(1, n+1, 2):
        if n % i == 0:
            answer += 1
    return answer

# a부터 k개의 연속된 수의 합
# a + (a+1) + (a+2) + ... + (a+k-1) = n
# n = (2a + k - 1) * k / 2
# a = n/k + (1-k)/2
# a가 자연수가 되려면 k는 n의 약수, k는 홀수여야 한다.
