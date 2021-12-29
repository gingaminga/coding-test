def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        value = []
        for j in range(len(arr1[i])):
            value.append(arr1[i][j] + arr2[i][j])
        answer.append(value)
            
    return answer

solution([[1,2],[2,3]], [[3,4],[5,6]]) # [[4,6],[7,9]]
solution([[1],[2]], [[3],[4]]) # [[4],[6]]

# https://programmers.co.kr/learn/courses/30/lessons/12950