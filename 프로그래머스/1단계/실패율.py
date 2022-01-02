def solution(N, stages):
    answer = []
    challengerAllCount = len(stages)  # 총 인원 수

    challengerOfstep = {}  # 단계별 도전자 수
    for stage in stages:
        challengerOfstep[stage] = challengerOfstep[stage] + \
            1 if stage in challengerOfstep else 1

    for i in range(1, N + 1):
        if i not in challengerOfstep:
            challengerOfstep[i] = 0

    challengerOfstepArray = sorted(challengerOfstep.items())

    failureRatio = 0  # 실패율

    for step, challengerCount in challengerOfstepArray:
        if step == N + 1:
            break

        failureRatio = challengerCount / challengerAllCount if challengerAllCount > 0 else 0
        challengerAllCount -= challengerCount
        answer.append((step, failureRatio))

    answer.sort(key=lambda x: (-x[1], x[0]))
    return [step for step, failureRatio in answer]


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])  # [3,4,2,1,5]
solution(4, [4, 4, 4, 4, 4])  # [4,1,2,3]

# https://programmers.co.kr/learn/courses/30/lessons/42889
