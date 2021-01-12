def solution(strings, n):
    answer = []
    a = []
    for i in strings:
        t = i[n] + i[0:n] + i[n+1:]
        a.append(t)
    a.sort()
    for i in a:
        t = i[1:n+1] + i[0] + i[n+1:]
        answer.append(t)
    return answer