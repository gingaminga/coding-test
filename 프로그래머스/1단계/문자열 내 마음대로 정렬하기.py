def solution(strings, n):
    return sorted(strings, key=lambda strings: (strings[n], strings))


solution(["sun", "bed", "car"], 1)  # ["car", "bed", "sun"]
solution(["abce", "abcd", "cdx"], 2)  # ["abcd", "abce", "cdx"]

# https://programmers.co.kr/learn/courses/30/lessons/12915
