def solution(n, words):
    answer = []
    index = -1
    history = [words[0]]

    for i in range(1, len(words)):
        # 앞사람이 말한 단어의 마지막 문자로 시작하는가?
        if history[-1][-1] != words[i][0]:
            index = i
            break

        # 이미 말한 단어인가?
        if words[i] not in history:
            history.append(words[i])
        else:
            index = i
            break

    if index == -1:
        answer = [0,0]
    else:
        a = index % n + 1
        b = index // n + 1
        answer = [a,b]

    return answer
