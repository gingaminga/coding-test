def solution(numbers):
    answer = []

    for key1, value1 in enumerate(numbers):
        for key2, value2 in enumerate(numbers):
            if value1 == value2 and key1 == key2:
                continue
            answer.append(value1 + value2)

    return sorted(list(set(answer)))


solution([2, 1, 3, 4, 1])  # [2,3,4,5,6,7]
solution([5, 0, 2, 7])  # [2,5,7,9,12]

# https://programmers.co.kr/learn/courses/30/lessons/68644
