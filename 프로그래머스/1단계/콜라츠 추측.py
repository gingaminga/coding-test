def solution(num):
    answer = 0
    
    while(num != 1):
        if(answer >= 500):
            answer = -1
            break;
        
        if(num % 2 == 0):
            # 짝수
            num = num//2
        else:
            # 홀수
            num = num * 3 + 1
        
        answer += 1

    return answer

solution(6) # 8
solution(16) # 4
solution(626331) # -1

# https://programmers.co.kr/learn/courses/30/lessons/12943