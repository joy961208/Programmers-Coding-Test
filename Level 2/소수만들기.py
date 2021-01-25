import math
from itertools import combinations

def prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    a = list(combinations(nums,3))
    for i in a:
        if prime(sum(i)):
            answer += 1

    return answer