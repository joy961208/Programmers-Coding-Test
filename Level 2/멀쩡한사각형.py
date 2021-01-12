import math
def solution(w,h):
    answer = w*h
    answer -= w+h-math.gcd(w,h)
    return answer
