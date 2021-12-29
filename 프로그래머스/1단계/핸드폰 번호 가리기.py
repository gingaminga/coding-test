def solution(phone_number):    
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

solution("01033334444") # *******4444
solution("027778888") # *****8888

# https://programmers.co.kr/learn/courses/30/lessons/12948