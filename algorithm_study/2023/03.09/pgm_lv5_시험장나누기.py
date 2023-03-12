# https://velog.io/@geunwoobaek/%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%8B%9C%ED%97%98%EC%9E%A5-%EB%82%98%EB%88%84%EA%B8%B0
# https://blog.encrypted.gg/1003
# https://ltk3934.tistory.com/184

# 처음: K만큼 잘랐을때 그룹의 합들중 최대값이 가장 적은 최솟값을 구한다.
# 바뀐문제: 그룹의 합의 최대값이 L보다 적거나 같을때 그 횟수가 K보다 작거나 같음을 만족하는 최대 L을 구한다.

import sys

sys.setrecursionlimit(10**8)


def solution(k, num, links):
    answer = 0
    root_candidate = [True for i in range(len(num))]
    dp = [None for i in range(len(num))]
    max_sum = sum(num)

    # 자식 노드로 거론되지 않은 노드 찾기
    # links 배열에 등장하면 자식 노드이므로 False 처리
    for a, b in links:
        for i in (a, b):
            if i >= 0:
                root_candidate[i] = False

    root = None
    for i in range(len(root_candidate)):
        if root_candidate[i]:
            root = i
            break

    def dfs(root, lower_bound):
        left, right = links[root]
        if dp[root] != None:
            return dp[root]

        dp_left, dp_right = [
            dfs(i, lower_bound) if i != -1 else [max_sum, 0] for i in [left, right]
        ]

        all_sum = num[root] + dp_left[0] + dp_right[0]
        two_sum = num[root] + min(dp_left[0], dp_right[0])

        if all_sum <= lower_bound:
            dp[root] = all_sum, dp_left[1] + dp_right[1] - 1
        elif two_sum <= lower_bound:
            dp[root] = two_sum, dp_left[1] + dp_right[1]
        else:
            dp[root] = num[root], dp_left[1] + dp_right[1] + 1
        return dp[root]

    left, right = max(num), max_sum
    while left < right:
        dp = [None for _ in range(len(num))]
        # 나누기 2의 내림값
        mid = (left + right) >> 1
        result = dfs(root, mid)
        if result[1] <= k:
            right = mid
        else:
            left = mid + 1
    print(left)
    return left

    return answer


# solution(
#     3,
#     [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
#     [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]])

solution(
    1,
    [6, 9, 7, 5],
    [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
)
