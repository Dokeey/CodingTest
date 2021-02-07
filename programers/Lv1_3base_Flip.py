'''
45
1       2        0       0
3^3*1 + 3^2*2 + 3^1*0 + 3^0*0
'''


def solution(n):
    base_stack = []
    while True:
        if n < 3:
            base_stack.append(n)
            break
        else:
            num = n % 3
            n //= 3
            base_stack.append(num)
    return int(''.join(map(str, base_stack)), base=3)


n = 1
print(solution(n))
