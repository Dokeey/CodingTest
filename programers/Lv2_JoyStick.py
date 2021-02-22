'''
1. 이동
- 왼쪽으로 가느냐, 오른쪽으로 가느냐 정하기
    - 주의: 마지막 인덱스에서 오른쪽방향으로 간다해도 첫 인덱스로 갈 수 없음.
    - A가 가장 많은 구간의 길이 / 시작, 끝 index를 기억한다.
    - 좌측 ~ A 시작점 길이와 A구간 길이를 비교하여 비용계산
2. 알파벳 고르기
- A~Z는 0~25 index 활용
- M을 기준 12번전 알파벳은 위로, 12번포함 이후는 아래로 (M을 아래로)

문자 케이스
ZAZAAAAAA...AAAAAAAZZZZZZZZZZZZZZZ
ZAAAZZZZAZAA
ZZZZAAAZZZ

AAAAZZAAA
ZZZZAZZZ

ABBBBAAAAABAAA 15
'''


def get_max_a_index(name):
    a_max, a_cnt, a_start, a_end = 0, 0, 0, 0

    for i, n in enumerate(name):
        if n == 'A':
            a_cnt += 1
        if a_max < a_cnt:
            a_max = a_cnt
            a_end = i
            a_start = i - a_cnt + 1
        if n != 'A':
            a_cnt = 0

    return a_start, a_end, a_max


def solution(name):
    # 이동한 값 구하기
    a_start, a_end, a_max = get_max_a_index(name)
    right_len = len(name[1:a_start])
    if a_max < right_len * 2:
        a_cnt = 0
        for n in reversed(name):
            if n == 'A': a_cnt += 1
            else: break
        cnt = len(name) - a_cnt - 1
    else:
        left_len = len(name[a_end + 1:])
        cnt = right_len * 2
        cnt += left_len

    # 알파벳 선택값 구하기
    AVG = (ord('Z') - ord('A')) // 2
    init_name = len(name) * 'A'
    for i in range(len(name)):
        if name[i] != init_name[i]:
            if AVG >= ord(name[i]) - ord(init_name[i]):
                cnt += ord(name[i]) - ord(init_name[i])
            else:
                cnt += ord('Z') - ord(name[i]) + 1

    return cnt


name = 'AAAAZZAAA'
print(solution('M'))
print(solution('BBABAAAB'))
print(solution('ZZZZAZZZ'))  # 이동7, 변환7
# print(solution('ABABAAAAABA')) #10
# print(solution('ABAAAAABAB')) #8
# print(solution('ABABAAAAAB')) #8
# print(solution('AAA')) #0
# print(solution('ABAAAAAAABA')) #6
# print(solution('AAB')) #2
# print(solution('ZZZ')) #5
# print(solution('BBBBAAAAAB')) #10
# print(solution('BBBBAAAABA')) #12
