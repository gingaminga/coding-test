def solution(s):    
    pCount = 0
    yCount = 0
    
    for alphabet in s.lower(): 
        if alphabet == 'p':
            pCount += 1
        elif alphabet == 'y':
            yCount += 1

    return pCount == yCount

solution('pPoooyY') # true
solution('Pyy') # false

# https://programmers.co.kr/learn/courses/30/lessons/12916