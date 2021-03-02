def solution(s):
    answer = ''
    s = s.lower()
    a = list(s)
    a[0] = a[0].upper()

    for i,j in enumerate(a[:-1]):
        if j == " ":
            a[i+1] = a[i+1].upper()
    for i in a:
        answer += i
    return answer
