def solution(n):
    count = 1  # 2는 무조건 소수이기 때문에 미리 포함
    isDemical = True

    for num in range(3, n + 1, 2):
        isDemical = True
        for i in range(2, int(num ** (1/2)) + 1):
            if num % i == 0:
                isDemical = False
                break

        if isDemical:
            count += 1

    print(count)
    return count


solution(10)  # 4
solution(5)  # 3

# https://programmers.co.kr/learn/courses/30/lessons/12921
