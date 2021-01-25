def solution(s, n):
    answer = ''
    for i in list(s):
        if i == " ":
            answer += " "
            continue
        a = ord(i)
        if a <91:
            a += n
            if a>90:
                a -= 26
        else:
            a += n
            if a>122:
                a -= 26
        answer += chr(a)
    return answer