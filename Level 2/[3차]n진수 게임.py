def njinsu(a,n):
    li = []
    if a ==0 or a == 1:
        return [a]

    while a > 0:
        t = a%n

        if t == 10:
            t = "A"
        elif t == 11:
            t = "B"
        elif t == 12:
            t = "C"
        elif t == 13:
            t = "D"
        elif t == 14:
            t = "E"
        elif t == 15:
            t = "F"
        li.append(t)
        a = a//n
    li.reverse()
    return li

def solution(n, t, m, p):
    answer = ''
    li = []
    a = 0
    while True:
        for i in njinsu(a,n):
            li.append(str(i))
            if len(li) >= m*t:
                break
        if len(li) >= m*t:
            break
        a += 1
    for  i in range(t):
        answer += li[p-1]
        p += m
    return answer
