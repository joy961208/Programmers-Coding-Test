def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    while A:
        a = A.pop()
        b = B.pop(0)
        answer += a*b

    return answer