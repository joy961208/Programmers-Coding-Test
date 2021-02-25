import math
def solution(distance, rocks, n):
    answer = 0
    #바위를 거리로 분류하는 과정
    rocks.append(distance)
    rocks.sort()
    r = [rocks[0]]

    for i,j in enumerate(rocks[1:]):
        r.append(j - rocks[i])

    maxlen = distance
    minlen = 1

    while maxlen >= minlen:
        rock = r.copy()
        midlen = (maxlen+minlen)//2
        delrock = 0
        minrock = 0
        for i in rock:
            t = i+minrock
            if t < midlen:
                minrock += i
                delrock += 1
            else:
                minrock = 0
        if delrock > n:
            maxlen = midlen - 1
        else:
            answer = midlen
            minlen = midlen + 1
    return answer