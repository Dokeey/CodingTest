'''
입출력 예 #1

a와 b의 내적은 1*(-3) + 2*(-1) + 3*0 + 4*2 = 3 입니다.
'''


def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer


a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]
print(solution(a, b))
