def solution(numbers):
    answer = 0
    result = set()

    number_list = list(numbers)

    def permutation(target, arr):
        result = []
        visited = [False for _ in range(len(arr))]

        def nowPermute(nowArr):
            if len(nowArr) == target:
                if nowArr not in result:
                    result.append(nowArr)
                return
            for i in range(len(arr)):
                if not visited[i]:
                    visited[i] = True
                    nowPermute(nowArr + [arr[i]])
                    visited[i] = False

        nowPermute([])
        return result

    def is_prime_number(number):
        if number == 0 or number == 1:
            return False

        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return False
        return True

    for i in range(1, len(number_list)+1):
        permute_list = permutation(i, number_list)
        for element in permute_list:
            result.add(int("".join(element)))

    for number in list(result):
        if is_prime_number(number):
            answer += 1

    return answer
