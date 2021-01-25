from itertools import permutations
import math
def prime(a):
    if a == 1 or a == 0:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True

def solution(numbers):
    a = set()
    for i in range(1,len(numbers)+1):
        b = set(map(''.join, permutations(list(numbers),i)))
        for j in b:
            if prime(int(j)):
                a.add(int(j))
    return len(a)