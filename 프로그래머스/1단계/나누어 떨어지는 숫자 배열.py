def solution(arr, divisor):
    answer = sorted([num for num in arr if num % divisor == 0])
    return answer if len(answer) > 0 else [-1]

solution([5, 9, 7, 10], 5) # [5, 10]
solution([2, 36, 1, 3], 1) # [1, 2, 3, 36]
solution([3,2,6], 10) # [-1]

# https://programmers.co.kr/learn/courses/30/lessons/12910