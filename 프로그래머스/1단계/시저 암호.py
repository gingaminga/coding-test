def solution(sentence, n):
    answer = ''

    for s in sentence:
        if s.isalpha() is not True:
            # 공백
            answer += s
            continue

        code = ord(s)
        if (ord(s) >= ord('a') and ord(s) <= ord('z')) and (ord(s) + n > ord('z')):
            # 기존 a-z였던 경우에서 z의 아스키코드값인 122를 넘어간 경우
            code += n - 26
        elif (ord(s) >= ord('A') and ord(s) <= ord('Z')) and (ord(s) + n > ord('Z')):
            # 기존 A-Z였던 경우에서 Z의 아스키코드값인 90을 넘어간 경우
            code += n - 26
        else:
            code += n

        answer += chr(code)

    print(answer)
    return answer


solution("AB", 1)  # BC
solution("z", 1)  # a
solution("a B z", 4)  # e F d

# https://programmers.co.kr/learn/courses/30/lessons/12926
