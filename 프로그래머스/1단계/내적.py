def solution(a, b):
    return sum(num1 * num2 for (num1, num2) in zip(a,b))

solution([1,2,3,4], [-3,-1,0,2]) # 3
solution([-1,0,1], [1,0,-1]) # -2

# https://programmers.co.kr/learn/courses/30/lessons/70128