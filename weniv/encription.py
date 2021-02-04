'''
**문제 1**
다음과 같은 치환 암호가 있다. 알파벳은 편의상 F까지 밖에 없다고 가정한다.

A -> !
B -> @
C -> %
D -> J
E -> L
F -> K

**입력**
ABCABCFFDD

**출력**
!@%!@%KKJJ

'''

d = {'A': '!',
     'B': '@',
     'C': '%',
     'D': 'J',
     'E': 'L',
     'F': 'K'}


def encription(input):
    return ''.join([d[i] for i in input])


print(encription('ABCABCFFDD'))
