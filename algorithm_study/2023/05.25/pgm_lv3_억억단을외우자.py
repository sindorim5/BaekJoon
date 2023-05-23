# from collections import defaultdict
# import math

"""
# 70점
def solution(e, starts):
    answer = []

    dict = defaultdict(int)
    min_start = min(starts)

    for num in range(min_start, e+1):
        dict[num] = submultiple(num)

    for start in starts:
        temp_key = float('inf')
        temp_value = -1
        for (key, value) in dict.items():
            if key < start:
                continue
            if value > temp_value:
                temp_key = key
                temp_value = value
        answer.append(temp_key)
    return answer
"""

"""
# 80점
def solution(e, starts):
    answer = []

    dict = defaultdict(int)
    min_start = min(starts)

    for num in range(min_start, e+1):
        dict[num] = submultiple(num)


    sorted_dict = sorted(dict.items(), key= lambda x: x[1], reverse=True)

    for start in starts:
        for key, value in sorted_dict:
            if key >= start:
                answer.append(key)
                break
    return answer
"""


"""
def submultiple(num):
    root_num = math.sqrt(num)
    count = 0

    for i in range(1, int(root_num)+1):
        if (num % i == 0):
            count += 2

    if (num % root_num == 0):
        count -= 1

    return count
"""

"""
# 90점
from collections import defaultdict

def solution(e, starts):
    answer = []

    dict = defaultdict(lambda: 1)

    dict[1] = 1

    for i in range(2, e+1):
        for j in range(1, e+1):
            if (i * j > e):
                break
            dict[i * j] += 1

    sorted_dict = sorted(dict.items(), key= lambda x: x[1], reverse=True)

    for start in starts:
        for key, value in sorted_dict:
            if (key >= start):
                answer.append(key)
                break

    return answer
"""


def solution(e, starts):
    result = []
    divisor = [1 for _ in range(e+1)]
    memo = 0
    starts_dict = {}
    sorted_starts = sorted(starts)

    for i in range(2, e+1):
        for j in range(i, e+1, i):
            divisor[j] += 1

    for i in range(len(sorted_starts)):
        if memo == 0:
            max_index = divisor[sorted_starts[i]:].index(
                max(divisor[sorted_starts[i]:])
            ) + sorted_starts[i]
            starts_dict[sorted_starts[i]] = max_index
            memo = max_index
        else:
            if sorted_starts[i] <= memo:
                starts_dict[sorted_starts[i]] = memo
            else:
                memo = divisor[sorted_starts[i]:].index(
                    max(divisor[sorted_starts[i]:]))+sorted_starts[i]
                starts_dict[sorted_starts[i]] = memo
        print(i, starts_dict, sorted_starts)

    for s in starts:
        result.append(starts_dict.get(s))

    return result
