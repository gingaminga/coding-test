def solution(arr):
    arr.remove(min(arr))
    
    if len(arr) < 1:
        arr = [-1]
    
    return arr

solution([4,3,2,1]) # [4,3,2]
solution([10]) # [-1]

# https://programmers.co.kr/learn/courses/30/lessons/12935