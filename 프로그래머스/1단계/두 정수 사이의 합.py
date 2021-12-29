def solution(a, b):
    answer = 0
    
    start = a
    end = b
    if a > b:
        start = b
        end = a
    elif a == b:
        return a
    
    return sum([i for i in range(start, end + 1)])

solution(3, 5) # 12
solution(3, 3) # 3
solution(5, 3) # 12

# https://programmers.co.kr/learn/courses/30/lessons/12912