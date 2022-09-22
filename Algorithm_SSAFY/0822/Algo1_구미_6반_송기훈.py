T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    maxValue = 0
    count = 0
    i = 0
    flag = 0

    while i < len(numbers) - 1:
        # 높은 수 -> 낮은 수
        if flag == 0:
            if numbers[i] > numbers[i + 1]:
                count += 1
                flag = 1

        # 골짜기 시작
        elif flag == 1:
            if numbers[i] >= numbers[i + 1]:
                count += 1
            elif numbers[i] < numbers[i + 1]:
                count += 1
                flag = 2

        # 낮은 수 -> 높은 수
        elif flag == 2:
            if numbers[i] < numbers[i + 1]:
                count += 1
            else:
                # flag를 다시 0으로 초기화 하고 최대값을 저장한다
                flag = 0
                if maxValue < count:
                    maxValue = count
                    count = 0
        i += 1

    # 4번 테스트케이스와 같이 내려가는 수로 끝나는 것이 카운트 되지 않기위해
    # flag = 2일 때만 카운트
    # 3번 테스트케이스와 같이 마지막 수까지 골짜기인 경우를 위해 추가된 조건문
    if flag == 2:
        if count:
            count += 1
            if maxValue < count:
                maxValue = count
                count = 0

    print("#{} {}".format(test_case, maxValue))
