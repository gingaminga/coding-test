def solution(n):
    demicals = [True] * n

    demicals[0] = False
    for i in range(2, int(n ** (1/2)) + 1):
        if demicals[i - 1]:
            for j in range(i * 2, n + 1, i):
                demicals[j - 1] = False

    print(demicals.count(True))
    return demicals.count(True)


solution(10)  # 4
solution(5)  # 3

# https://programmers.co.kr/learn/courses/30/lessons/12921

# 에라토스테네스의 체
# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
