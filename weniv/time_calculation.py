'''
1. 한 배에는  탈 수 있는 인원이 정시에는 25명, 10분마다 15명씩 탈 수 있습니다.
2. 배는 매일 9시부터 21시 전까지(21시를 포함하지 않습니다) 10분단위로 들어옵니다.
3. 전체 대기 인원은 14,000,605명입니다. 우리는 14,000,606번째와 14,000,607번째에 배를 타게 됩니다. 앞사람이 아프거나, 대기를 못하고 빠질 경우 대기인원이 줄어들 수도 있습니다.
**라이캣과 자바독이 다른 배를 타야 할 경우에는 뒷배를 타야 합니다.**
4. 1월은 1024일, 2월은 512일, 3월은 256일, 4월은 128일, 5월은 64일, 6월은 32일, 7월은 16일, 8월은 8일, 9월은 4일, 10월은 2일이며, 10월까지밖에 없습니다.
5. 시간의 개념은 동일합니다. (하루는 24시간, 1시간 60분, 1분 60초)
    - **현재 날짜는 2020년 1월 1일 입니다.**
6. 배에 타는 순간 자바독이 화장실이 급하다 하여 화장실에 갔으며, 현재시간에 '분'만큼 배 출발이 늦어졌습니다.
7. 배는 휴일도 동일하게 운항됩니다. 배는 천재지변에 영향을 받지 않습니다. 마법으로 날아다니거든요.
8. **라이캣과 자바독이 배에 타는 날짜를 구하세요.**

    ```python
    **입력**
    대기인원 = 14000605

    **출력**
    2025년 2월 413일 11시 0분 출발

    **입력**
    대기인원 = 1200202

    **출력**
    2020년 1월 1000일 11시 0분 출발

    ```
'''
'''
요약 정리하자

00 10 20 30 40 50 : 1시간당
25 15 15 15 15 15 : 100명 수용

운영시간 : 9시~20시 50분까지 10분단위로 들어옴. = 하루에 총 12시간 = 1200명 수용
대기인원 : 14,000,605
> 현재순번 / 1200 = 걸리는 날
> 현재순번 % 1200 = 마지막날 대기 인원
날짜 개념 : 1월은 1024일, 2월은 512일, 3월은 256일, 4월은 128일, 5월은 64일, 6월은 32일, 7월은 16일, 8월은 8일, 9월은 4일, 10월은 2일
현재 날짜 : 2020년 1월 1일

애매한 조건 : 3번의 두번째 문단, 6번 조건이 뭘 말하고 싶은건지 모르겠다.
'''


def find_day(total_day):
    first_month = 2048
    year = 0
    month = 1

    while True:
        first_month = first_month / 2
        total_day -= first_month

        if total_day < 0:
            total_day += first_month
            break
        if first_month == 2:
            first_month = 2048
            year += 1
        month += 1

    return year, month % 10, int(total_day)


def find_time(waiters):
    capacity_per_minute = [25, 10, 10, 10, 10, 10]
    hour = int(waiters / 100)
    last_hour_waiter = waiters % 100
    minuts = 0

    for capa in capacity_per_minute:
        last_hour_waiter -= capa
        if last_hour_waiter < 0:
            last_hour_waiter += capa
            break
        minuts += 10
    return hour + 9, minuts


# WAITERS = 14000605
WAITERS = 1200202
total_day = int(WAITERS / 1200)
last_day_waiters = WAITERS % 1200

year, month, day = find_day(total_day)
hour, minuts = find_time(last_day_waiters)
print(f'{year}년 {month}월 {day}일 {hour}시 {minuts}분 출발')
