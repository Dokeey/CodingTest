"""
재귀를 이용한 sum 구현
"""


def sum(x: list):
    if x:
        num = x.pop()
        return num + sum(x)
    return 0


print(sum([2, 5, 2, 7]))
print(sum([]))
