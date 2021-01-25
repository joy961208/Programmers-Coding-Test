def solution(s):
    answer = ''
    a = list(s)
    a.sort()
    a.reverse()
    for i in a:
        answer += i
    return answer