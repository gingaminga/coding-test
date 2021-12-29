def solution(n):    
    x = n**(1/2)    
    return (x + 1) * (x + 1) if x.is_integer() else -1

solution(121) # 144
solution(3) # -1

# https://programmers.co.kr/learn/courses/30/lessons/12934