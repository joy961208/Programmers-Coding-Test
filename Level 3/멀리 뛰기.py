def solution(n):
    a = 1
    b = 2
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    for i in range(n-2):
        c = a + b
        a = b
        b = c
    return c%1234567
