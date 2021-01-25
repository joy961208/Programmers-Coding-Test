def solution(n):
    a = list(str(n))
    a.sort()
    a.reverse()
    c = ""
    for i in a:
        c += str(i)
    return int(c)