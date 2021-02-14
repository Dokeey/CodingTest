'''
입력 : "()))((()"
결과 : "()(())()"
'''


def slice_string(p):
    string = ''
    while p:
        string += p.pop(0)
        if string.count('(') and string.count('(') == string.count(')'):
            return string
    return string


def correct_string(string):
    check = []
    for s in string:
        if s == '(':
            check.append(s)
        else:
            if '(' not in check:
                return False
            check.remove('(')

    if not check:
        return True
    return False


def reverse_string(string):
    return ''.join(list(map(lambda x: '(' if x == ')' else ')', string)))


def solution(p):
    if not p: return p
    p = list(p)
    u = slice_string(p)
    v = ''.join(p)

    if correct_string(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse_string(u[1:-1])


p = "()))((()"
print(solution(p))
