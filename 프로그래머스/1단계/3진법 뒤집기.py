def solution(n):
    ternary = []

    if n < 3:
        # n이 3진법 수보다 작을 경우
        ternary.append(n)

    while n >= 3:
        remainder = n % 3  # 나머지
        n = n // 3  # 몫

        ternary.append(remainder)
        if n < 3:
            ternary.append(n)

    ternary.reverse()

    print(sum([ternary[i] * (3 ** i) for i in range(len(ternary))]))
    return sum([ternary[i] * (3 ** i) for i in range(len(ternary))])


solution(45)  # 7
solution(125)  # 229

# https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3
