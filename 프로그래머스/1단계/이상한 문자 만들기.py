def solution(s):
    answer = ''
    
    index = 0
    for word in s:
        if word.isspace():
            index = 0
            answer += word
            continue

        if index % 2 == 0:
            answer += word.upper()
        else:
            answer += word.lower()
        index += 1
    
    print(answer)
    return answer

solution("try hello world") # TrY HeLlO WoRlD

# https://programmers.co.kr/learn/courses/30/lessons/12930