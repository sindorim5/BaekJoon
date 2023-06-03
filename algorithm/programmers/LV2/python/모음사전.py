order = 0


def dfs(now_word, dict, alpha):
    global order
    if len(now_word) > 5:
        return

    dict[now_word] = order
    order += 1

    for char in alpha:
        dfs(now_word + char, dict, alpha)


def solution(word):
    global order
    alpha = ['A', 'E', 'I', 'O', 'U']
    dict = {}

    dfs("", dict, alpha)

    return dict[word]


print(solution("AAA"))
