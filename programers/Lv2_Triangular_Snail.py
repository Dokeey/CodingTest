'''
n = 6일때 규칙!

while
    1번째
        0, 0 / 1, 0 / 2, 0 / 3, 0 ....
                    / 2, 1 / 3, 1 ....
    n = n - 1

    2번째
        5, 1 / 5, 2 / 5, 3 / 5, 4 ....
             / 4, 2 / 4, 3 ....
    n = n - 1

    3번째
        4, 4 / 3, 3 / 2, 2 / 1, 1 ....
             / 3, 2 ...
    n = n - 1
'''


def solution(n):
    rows = [[0 for _ in range(i)] for i in range(1, n + 1)]
    cnt = 0
    first_start = 0
    first_val = 0
    second_start = 1
    second_val = n - 1
    third_start = n - 2
    third_val = 0
    while n:
        # 첫번째
        for i in range(first_start, n + first_start):
            cnt += 1
            rows[i][first_val] = cnt
        first_start += 2
        first_val += 1
        n -= 1
        if n < 1: break

        # 두번째
        for i in range(second_start, n + second_start):
            cnt += 1
            rows[second_val][i] = cnt
        second_start += 1
        second_val -= 1
        n -= 1
        if n < 1: break

        # 세번째
        for i in range(n):
            cnt += 1
            rows[third_start - i][third_start - i - third_val] = cnt
        third_start -= 1
        third_val += 1
        n -= 1

    answer = []
    for row in rows: answer += row
    return answer


n = 7
print(solution(n))

# rows = [[0 for _ in range(i)] for i in range(1, n + 1)]
# print(rows)
