def solution(n, m):
    max_num, min_num = max(n, m), min(n, m)
    while max_num % min_num != 0:
        max_num, min_num = min_num, max_num % min_num

    return [min_num, n * m // min_num]


n = 3
m = 12
print(solution(n, m))
