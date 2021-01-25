import math
def solution(n):
    a = math.sqrt(n)
    if a.is_integer():
        return pow(a+1,2)
    else:
        return -1