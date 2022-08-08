def solution(want, number, discount):
    dic = {}
    answer = 0
    for i in range(len(want)):
        dic[want[i]] = number[i]

    maxIndex = len(discount) - 1
    for i in range(len(discount)):
        if (i + 9) > maxIndex:
            break

        tempDiscount = discount[i : i + 10]
        count = 0
        for w in want:
            if dic[w] == tempDiscount.count(w):
                count += 1
        if count == len(want):
            answer += 1

    return answer
