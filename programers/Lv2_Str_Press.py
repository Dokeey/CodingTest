'''
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17
'''
from math import ceil


def get_string_list(cut, s):
    result = []
    while s:
        string = s[:cut]
        result.append(string)
        s = s[cut:]
    return result


def solution(s):
    answer = ''
    answer_list = []
    len_s = len(s)
    for cut in range(1, ceil(len_s / 2) + 1):
        string_list = get_string_list(cut, s)
        cnt = 1
        first_string = string_list.pop(0)
        while string_list:
            if first_string != string_list[0]:
                if cnt == 1: cnt = ''
                answer += str(cnt) + first_string
                cnt = 1
                first_string = None
            else:
                string_list.pop(0)
                cnt += 1
            if not first_string:
                first_string = string_list.pop(0)
            if not string_list:
                if cnt == 1: cnt = ''
                answer += str(cnt) + first_string

        answer_list.append(answer)
        answer = ''

    return min(list(map(len, answer_list))) or 1


s = "ababcdcdababcdcd"
print(solution(s))
