def solution(progresses, speeds):
    answer = []
    a = progresses

    while True:
        if len(a) == 0:
            break
        c = 0
        cc = 0
        for i in range(len(a)):
            a[cc] += speeds[cc]
            if a[cc] >= 100 and cc == 0:
                c+=1
                a.remove(a[cc])
                speeds.remove(speeds[cc])
                cc -= 1
            cc += 1
        if c != 0:
            answer.append(c)


    return answer
