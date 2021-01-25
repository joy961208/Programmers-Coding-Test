def solution(N, stages):
    answer = []
    a = len(stages)
    for i in range(1,N+1):
        if a == 0:
            answer.append([0,i])
            continue
        t = stages.count(i)
        answer.append([t/a,i])
        a -= t

    answer.sort(key = lambda x: (x[0],-x[1]))
    answer.reverse()
    return [i[1] for i in answer]