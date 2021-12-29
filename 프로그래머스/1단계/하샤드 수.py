def solution(x):
    answer = True
    
    sum = 0
    for number in str(x):
        sum += int(number)
    
    if x % sum != 0:
        answer = False

    return answer

solution(10) # true
solution(12) # true
solution(11) # false
solution(13) # false

# https://programmers.co.kr/learn/courses/30/lessons/12947