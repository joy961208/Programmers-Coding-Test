def solution(x):
    a = list(str(x))
    b = 0
    for i in a:
        b += int(i)
    if x%b == 0:
        return True
    return False