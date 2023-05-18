def solution(A, B):
    answer = 0

    # 내림차순 정렬
    A.sort(reverse=True)

    # 오름차순 정렬, B는 pop()을 쓸껀데 pop(0)는 시간상 불리함
    B.sort(reverse=True)

    for a in A:
        # a가 B의 제일 큰 원소보다 크거나 같다면??
        # -> B[0]는 다음 상대를 찾아야 함
        if a >= B[-1]:
            continue
        # 이외의 경우는 이길 수 있는 경우
        else:
            answer += 1
            B.pop()

    return answer
