'''
1. 노란색으로 만들 수 있는 직사각형 패턴을 전부 찾는다.
2. 그 패턴들중 갈색 수와 맞는 패턴을 찾는다.

brown	yellow	return
10	    2	    [4, 3]
8	    1	    [3, 3]
24	    24	    [8, 6]
'''


def solution(brown, yellow):
    y_divs = [num for num in range(1, int(yellow ** 0.5) + 1) if yellow % num == 0]
    for div in y_divs:
        y_col = yellow // div
        currunt_brown = div * 2 + y_col * 2 + 4
        if brown == currunt_brown:
            return sorted([div + 2, y_col + 2], reverse=True)


brown = 10
yellow = 2
print(solution(brown, yellow))
