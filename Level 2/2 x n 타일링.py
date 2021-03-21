
def solution(n):
    a = 1
    b = 2

    for i in range(n-2):
        c = a+b
        a = b
        b = c

    return c%1000000007
