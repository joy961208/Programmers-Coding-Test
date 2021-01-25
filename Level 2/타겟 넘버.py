from  itertools import combinations
def solution(numbers, target):
    answer = 0
    s = sum(numbers)
    if s == target:
        answer += 1
    for i in range(1,len(numbers)):
        combi = list(combinations(numbers,i))
        for j in combi:
            if s - sum(j)*2 == target:
                answer += 1
    return answer