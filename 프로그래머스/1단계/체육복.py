def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    availableCount = n - len(lost)  # 현재 수업 참여 가능한 총 인원

    tmp = []
    for lostPeople in lost:
        if lostPeople in reserve:
            reserve.remove(lostPeople)
            tmp.append(lostPeople)
            availableCount += 1

    for tmpPeople in tmp:
        if tmpPeople in lost:
            lost.remove(tmpPeople)

    print(lost, reserve)

    for lostPeople in lost:
        if lostPeople - 1 in reserve:
            reserve.remove(lostPeople - 1)
            availableCount += 1
        elif lostPeople + 1 in reserve:
            reserve.remove(lostPeople + 1)
            availableCount += 1

    print(availableCount)
    print()
    return availableCount


solution(5, [2, 4], [1, 3, 5])  # 5
solution(5, [2, 4], [3])  # 4
solution(3, [3], [1])  # 2

# https://programmers.co.kr/learn/courses/30/lessons/42862
