'''
최대공약수를 이용한 공식 유도로 해결했어야 함..
수학적 사고력이 요구되어 방심했다가 이해하는데 역대급으로 어려웠다.
'''


def gcd(w, h):
    max_num, min_num = max(w, h), min(w, h)
    while max_num % min_num:
        max_num, min_num = min_num, max_num % min_num
    return min_num


def solution(w, h):
    g = gcd(w, h)
    return w * h - (w + h - g)


w = 499
h = 1000
print(solution(w, h))
