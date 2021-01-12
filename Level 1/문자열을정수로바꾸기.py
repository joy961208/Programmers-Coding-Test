def solution(s):
    if '-' in s:
        answer = -1*int(s[1:])
    elif '+' in s:
        answer = int(s[1:])
    else:
        answer = int(s)
    return answer
