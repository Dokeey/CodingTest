''' 문제
1. 이 간선들을 2진 깊이우선 탐색하며 작은 값만을 선택해서, 또는 큰 값만을 선택해서 내려와야 합니다.
2. 아래 결과값을 단서로 삼아 다음 미션지로 향하세요! 단, 코드로 풀어야 합니다.
'''
'''
DFS 스택을 이용
조건 : 스택에 담았던 노드는 더 이상 스택에 담지 않는다.
조건2: 방문했던 노드도 더 이상 스택에 담지 않는다.

START : 첫 노드를 스택에 쌓는다.
while stack:
    1. 스택에서 노드를 꺼낸다. 방문 안했다면 방문했다는 표시를 한다.
    2. 자식 중 스택에 없고, 방문안했던 노드를 전부 스택에 넣는다.
'''
graph = {100: set([67, 66]),
         67: set([100, 82, 63]),
         66: set([100, 73, 69]),
         82: set([67, 61, 79]),
         63: set([67]),
         73: set([66]),
         69: set([66, 65, 81]),
         61: set([82]),
         79: set([82, 87, 77]),
         65: set([69, 84, 99]),
         81: set([69]),
         87: set([79, 31, 78]),
         77: set([79]),
         84: set([65]),
         99: set([65]),
         31: set([87]),
         78: set([87])}


def only_max_dfs(first_node):
    # START
    stack = [first_node]
    visit = []

    # 순회
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            nums = list(graph[node] - set(stack) - set(visit))
            if not nums:
                break
            stack.append(max(nums))
    return visit


def only_min_dfs(first_node):
    # START
    stack = [first_node]
    visit = []

    # 순회
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            nums = list(graph[node] - set(stack) - set(visit))
            if not nums:
                break
            stack.append(min(nums))
    return visit


max_visits = only_max_dfs(100)
min_visits = only_min_dfs(100)

print(''.join(list(map(chr, max_visits))))
print(''.join(list(map(chr, min_visits))))
