def solution(n):
    answer = n
    binaryN = bin(n)
    count = binaryN.count('1')
    while True:
        answer += 1
        binaryAnswer = bin(answer)
        if count == binaryAnswer.count('1'):
            break

    return answer

