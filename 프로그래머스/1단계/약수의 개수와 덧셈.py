def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count % 2 == 0:
            # 짝수
            answer += num
        else:
            # 홀수
            answer -= num

    print(answer)
    return answer


solution(13, 17)  # 43
solution(24, 27)  # 52
solution(1, 2)  # 52

# https://programmers.co.kr/learn/courses/30/lessons/77884
