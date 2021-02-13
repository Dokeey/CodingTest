"""
결과 : ["AC", "ACDE", "BCFG", "CDE"]
"""
from itertools import combinations


def solution(orders, course):
    menu_cnt = {}
    answer = []

    for cnt in course:
        for order in orders:
            for menu in combinations(order, cnt):
                menu = ''.join(sorted(menu))
                if menu not in menu_cnt.keys(): menu_cnt[menu] = 1
                else: menu_cnt[menu] += 1

        sort_menu = sorted(menu_cnt.items(), key=lambda x: x[1], reverse=True)
        max_menu = []
        for menu in sort_menu:
            if max_menu:
                if max_menu[-1][1] > menu[1]: break
            if menu[1] >= 2: max_menu.append(menu)

        for menu in max_menu: answer.append(menu[0])
        menu_cnt = {}

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
