def solution(s):
    answer = True
    a = s.lower()
    a =list(a)
    y = a.count('y')
    p = a.count('p')
    if y != p:
        return False
    return True