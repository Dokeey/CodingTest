'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
'''


def solution(board, moves):
    stack = []
    result = 0
    for move in moves:
        for i, row in enumerate(board):
            doll = row[move - 1]
            if doll != 0:
                board[i][move - 1] = 0
                if stack:
                    if stack[-1] == doll:
                        stack.pop()
                        result += 2
                        break
                stack.append(doll)
                break

    return result


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
