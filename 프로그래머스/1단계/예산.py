def solution(d, budget):
    departmentsMoney = sorted(d)
    price = 0
    count = 0
    for money in departmentsMoney:
        price += money
        if price > budget:
            # 예산 초과
            break
        count += 1

    print(count)
    return count


solution([1, 3, 2, 5, 4], 9)  # 3
solution([2, 2, 3, 3], 10)  # 4

# https://programmers.co.kr/learn/courses/30/lessons/12982
