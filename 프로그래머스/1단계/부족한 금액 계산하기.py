def solution(price, money, count):   
    allPrice = price * sum([i for i in range(1, count + 1)])

    return allPrice - money if allPrice - money > 0 else 0

solution(3, 20, 4) # 10

# https://programmers.co.kr/learn/courses/30/lessons/82612