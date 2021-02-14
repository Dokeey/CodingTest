'''
1. 순열을 통해 숫자의 가짓수를 뽑아냄
2. 그 수들이 소수인지 판별
    - 2부터 제곱근까지 나누어보기 방법

입력 : "17"
결과 : 3
'''
from itertools import permutations


def check_prime_number(number):
    if number == 1 or number == 0: return False
    square = int(number ** (1 / 2))
    for s in range(2, square + 1):
        if number % s == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for cnt in range(1, len(numbers) + 1):
        for number in permutations(numbers, cnt):
            number = int(''.join(number))
            if number in answer: continue
            check = check_prime_number(number)
            if check:
                answer.append(number)
    return len(answer)


numbers = "011"
print(solution(numbers))
