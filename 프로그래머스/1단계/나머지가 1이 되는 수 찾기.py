def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i
        
    return 0

solution(10) # 3
solution(12) # 11

# https://programmers.co.kr/learn/courses/30/lessons/87389