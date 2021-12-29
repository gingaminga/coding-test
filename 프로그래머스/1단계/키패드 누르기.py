def solution(numbers, hand):
    answer = ''
    
    left = [1, 4, 7]
    right = [3, 6, 9]
    middle = [2, 5, 8, 0]
    leftPosition = (3, 0) # (row, col)
    rightPosition = (3, 2) # (row, col)
    
    for i in range(len(numbers)):
        if numbers[i] in left:
            # 무조건 왼손
            answer += 'L'
            leftPosition = (left.index(numbers[i]), 0)
        elif numbers[i] in right:
            # 무조건 오른손
            answer += 'R'
            rightPosition = (right.index(numbers[i]), 2)
        else:
            # 가운데인 경우
            nextPosition = (middle.index(numbers[i]), 1)
            
            leftCount = abs(leftPosition[0] - nextPosition[0]) + abs(leftPosition[1] - nextPosition[1]) # 왼쪽손 이동 예상 횟수
            rightCount = abs(rightPosition[0] - nextPosition[0]) + abs(rightPosition[1] - nextPosition[1]) # 오른쪽손 이동 예상 횟수 
            
            if leftCount == rightCount:
                if hand == 'left':
                    answer += 'L'
                    leftPosition = (middle.index(numbers[i]), 1)
                else:
                    answer += 'R'
                    rightPosition = (middle.index(numbers[i]), 1)
            elif leftCount > rightCount:
                # 왼쪽이 많은 경우 오른쪽 손 이용
                answer += 'R'
                rightPosition = (middle.index(numbers[i]), 1)
            else :
                # 오른쪽이 많은 경우 왼쪽 손 이용
                answer += 'L'
                leftPosition = (middle.index(numbers[i]), 1)            
            
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") # LRLLLRLLRRL
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") # LRLLRRLLLRR
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") # LLRLLRLLRL

# https://programmers.co.kr/learn/courses/30/lessons/67256