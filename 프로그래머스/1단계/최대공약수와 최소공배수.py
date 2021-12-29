def solution(n, m):    
    main = min(n, m)
    sub = max(n, m)
    
    while(sub):
        main, sub = sub, main % sub
    
    return [main, (n * m) // main]

solution(3, 12) # [3, 12]
solution(2, 5) # [1, 10]

# https://programmers.co.kr/learn/courses/30/lessons/12940