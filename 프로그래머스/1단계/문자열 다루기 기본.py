def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()

    return False

solution("a234") # false
solution("1234") # true

# https://programmers.co.kr/learn/courses/30/lessons/12918