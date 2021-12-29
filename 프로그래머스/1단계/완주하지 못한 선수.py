def solution(participant, completion):
    participant.sort()
    completion.sort()
    for (part,comp) in zip(participant, completion):
        if part != comp:
            return part

    return participant.pop()

solution(["leo", "kiki", "eden"], ["eden", "kiki"]) # leo
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) # vinko
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) # mislav

# https://programmers.co.kr/learn/courses/30/lessons/42576