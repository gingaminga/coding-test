def solution(answers):
    answer = []
    questionCount = len(answers)
    
    one = [(i % 5) + 1 for i in range(questionCount)]
    print(one)
    
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    if len(two) > questionCount:
        # 문제가 조건보다 짧을 경우
        two = two[:questionCount]
    elif len(two) < questionCount:
        # 문제가 조건보다 긴 경우
        two = two * (questionCount // len(two) + 1)
        two = two[:questionCount]
    print(two)   
    
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    if len(three) > questionCount:
            # 문제가 조건보다 짧을 경우
        three = three[:questionCount]
    elif len(three) < questionCount:
        # 문제가 조건보다 긴 경우
        three = three * (questionCount // len(three) + 1)
        three = three[:questionCount] 
    print(three)
    
    oneCount = 0
    twoCount = 0
    threeCount = 0
       
    for i in range(len(answers)):
        if one[i] == answers[i]:
            oneCount += 1
        if two[i] == answers[i]:
            twoCount += 1
        if three[i] == answers[i]:
            threeCount += 1
    
    result = [oneCount, twoCount, threeCount]
    maxCount = max(result)
    
    for i in range(len(result)):
        if maxCount == result[i]:
            # 많이 맞춘 정답자 색출
            answer.append(i + 1)

    print(answer)
    return answer

solution([1,2,3,4,5, 1,3,2,4,2]) # [1]
solution([1,3,2,4,2]) # [1,2,3]

# https://programmers.co.kr/learn/courses/30/lessons/42840