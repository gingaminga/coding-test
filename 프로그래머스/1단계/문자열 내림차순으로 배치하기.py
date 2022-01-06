def solution(setence):

    # 아스키코드로 변환 후 정렬
    toAscii = sorted([ord(s) for s in setence], reverse=True)

    # 문자열로 변경
    return ''.join([chr(s) for s in toAscii])


solution("Zbcdefg")  # gfedcbZ

# https://programmers.co.kr/learn/courses/30/lessons/12917
