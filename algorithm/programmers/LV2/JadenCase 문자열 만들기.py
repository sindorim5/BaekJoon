def solution(s):
    s = s.split(' ')
    temp = []
    for element in s:
        element = element.capitalize()
        temp.append(element)
    return ' '.join(temp)
