import datetime


def solution(a, b):
    weekend = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return weekend[datetime.date(2016, a, b).weekday()]


solution(5, 24)  # TUE

# https://programmers.co.kr/learn/courses/30/lessons/12901?language=javascript
