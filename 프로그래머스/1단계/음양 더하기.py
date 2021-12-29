def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
        
    return answer

solution([4,7,12], [True,False,True]) # 9
solution([1,2,3], [False,False,True]) # 0

# https://programmers.co.kr/learn/courses/30/lessons/76501
