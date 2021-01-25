def solution(s):
    a = len(s)
    if a%2 == 0:
        answer = s[(a//2)-1:(a//2)+1]
    else:
        answer = s[a//2]
    return answer