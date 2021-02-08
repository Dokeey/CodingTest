import re


def solution(dartResult):
    p = re.compile("[0-9]+[SDT][*#]?")
    group = p.findall(dartResult)
    bonus_dict = {'S': 1, 'D': 2, 'T': 3}
    answer = []

    for round in group:
        option = ''
        if round[-1] in ["*", "#"]:
            option = round[-1]
            round = round[:-1]
        bonus = round[-1]
        score = int(round[:-1])
        num = score ** bonus_dict[bonus]
        if option == '#':
            num *= -1
        elif option == '*':
            num *= 2
            if answer: answer[-1] *= 2

        answer.append(num)
    return sum(answer)


# dartResult = '1D2S#10S'
dartResult = '1S2D*3T'
# dartResult = '1S*2T*3S'
print(solution(dartResult))
