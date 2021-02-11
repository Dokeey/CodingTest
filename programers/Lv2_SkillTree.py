cache = []


def check_tree(skill_tree, skill, s):
    s_index = skill.index(s)
    if s in cache:
        return True
    if s_index != 0:
        t_index = skill_tree.index(s)
        if skill[s_index - 1] in skill_tree[:t_index]:
            cache.append(s)
            return check_tree(skill_tree, skill, skill[s_index - 1])
        return False
    cache.append(s)
    return True


def solution(skill, skill_trees):
    skill = list(skill)
    answer = len(skill_trees)
    for skill_tree in skill_trees:
        for s in skill_tree:
            if s in skill:
                if not check_tree(skill_tree, skill, s):
                    answer -= 1
                    break
                if s == skill[-1]:
                    break
        cache.clear()
    return answer


skill = "CBD"
skill_trees = ["DCA", "BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))

'''
결과 : 2

너무 어렵게 생각했다.
당연히 효율성을 따질것같아 고려하려다 보니 동적 프로그래밍 개념이랑 이것저것 적용할수 있을거같아 캐시를 사용했다.
그리고 다 짜고나니 다른분들보다 코드가 너무 길고 많다..
'''
