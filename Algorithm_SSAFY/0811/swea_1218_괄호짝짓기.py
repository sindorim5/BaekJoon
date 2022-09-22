import sys

sys.stdin = open(
    "C:/SSAFY/clone/Algorithm_SSAFY/0811/input_1218.txt", "r", encoding='utf-8')

T = 10
for test_case in range(1, T+1):
    # '()', '[]', '{}', '<>'
    n = int(input())
    text = list(input())

    left1 = "("
    right1 = ")"
    left2 = "["
    right2 = "]"
    left3 = "{"
    right3 = "}"
    left4 = "<"
    right4 = ">"

    temp = [left1, left2, left3, left4, right1, right2, right3, right4]
    dic = dict()

    for e in temp:
        dic[e] = 0

    for t in text:
        dic[t] += 1

    if (dic[left1] == dic[right1]
        and dic[left2] == dic[right2]
        and dic[left3] == dic[right3]
        and dic[left4] == dic[right4]
        ):
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))
