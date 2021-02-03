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

stone = [5, 3, 4, 1, 3, 8, 3]
# stone = [1, 2, 1, 4]
dogs = [{
    "이름": "루비독",
    "나이": "95년생",
    "점프력": "3",
    "몸무게": "4",
}, {
    "이름": "피치독",
    "나이": "95년생",
    "점프력": "3",
    "몸무게": "3",
}, {
    "이름": "씨-독",
    "나이": "72년생",
    "점프력": "2",
    "몸무게": "1",
}, {
    "이름": "코볼독",
    "나이": "59년생",
    "점프력": "1",
    "몸무게": "1",
},
]
for dog in dogs:
    for num in range(int(dog['점프력']) - 1, len(stone), int(dog['점프력'])):
        dog['die'] = False
        stone[num] -= int(dog['몸무게'])
        if stone[num] < 0:
            dog['die'] = True
            break

for dog in dogs:
    if dog['die'] == False:
        print(dog['이름'])
