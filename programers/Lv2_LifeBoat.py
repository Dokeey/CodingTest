'''
기존에 del people[0] 으로 맨앞 원소를 삭제했는데,
찾아보니 del은 O(n) 시간복잡도를 가지는것을 알았다.

deque로 변경하여 popleft로 효율성 해결!
'''

from collections import deque


def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    cnt = 0
    while people:
        min_man = people.pop()
        if limit < min_man * 2:
            cnt += len(people) + 1
            break
        for _ in range(len(people)):
            p = people.popleft()
            cnt += 1
            if limit >= p + min_man:
                break
        else:
            cnt += 1
    return cnt


people = [70, 80, 50]
limit = 100
# 결과 : 3

print(solution(people, limit))
