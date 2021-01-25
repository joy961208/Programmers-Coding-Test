def solution(n):
    answer = 0
    a = list(str(n))
    for i in a:
        answer += int(i)
    return answer