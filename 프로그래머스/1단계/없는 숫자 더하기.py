def solution(numbers):
    answer = 0
    
    allSum = 0
    for i in range(0,10):
        allSum += i
    
    numbersAllSum = 0
    for number in numbers:
        numbersAllSum += number
        
    answer = allSum - numbersAllSum
        
    return answer

solution([1,2,3,4,6,7,8,0]) # 14
solution([5,8,4,0,6,7,9]) # 6

# https://programmers.co.kr/learn/courses/30/lessons/86051