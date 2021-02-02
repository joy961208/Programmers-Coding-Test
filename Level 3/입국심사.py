def solution(n, times):
    answer = 0
    mintime = min(times)
    maxtime = mintime * n

    while maxtime >= mintime:
        num = 0
        midtime = (mintime + maxtime) // 2
        for i in times:
            num += midtime // i
            if num >= n:
                break
        if num >= n:
            maxtime = midtime - 1
            answer = midtime
        else:
            mintime = midtime + 1

    return answer