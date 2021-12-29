def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if i + 1 == len(arr):
            answer.append(arr[i])
            break

        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
        
    return answer

solution([1,1,3,3,0,1,1]) # [1,3,0,1]
solution([4,4,4,3,3]) # [4,3]

# https://programmers.co.kr/learn/courses/30/lessons/12906