def solution(n, lost, reserve):
    answer = n
    a = reserve.copy()
    b = lost.copy()
    for i in lost:
        if i in a:
            a.remove(i)
            b.remove(i)
    for i in b:
        if i-1 in a:
            a.remove(i-1)
        elif i+1 in a:
            a.remove(i+1)
        else:
            answer -= 1
    return answer
