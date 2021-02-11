from collections import deque


def solution(prices):
    queue = deque(prices)
    len_prices = len(prices)
    answer = []
    i = 0
    while queue:
        price = queue.popleft()
        i += 1
        time = None
        if price == 1:
            time = len_prices - i
        else:
            for j, q in enumerate(queue):
                if price > q:
                    time = j + 1
                    break
            if not time:
                time = len_prices - i
        answer.append(time)
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
'''
결과 : [4, 3, 1, 1, 0]
'''
