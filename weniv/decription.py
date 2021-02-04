'''문제 암호해독
섬으로 향하라!

'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

해(1)와 달(0),
Code의 세상 안으로!(En-Coding)
'''

str = ['   + -- + - + -   ',
       '   + --- + - +   ',
       '   + -- + - + -   ',
       '   + - + - + - +   ']
answer = ''.join([chr(int(s.replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for s in str])
print(answer)
