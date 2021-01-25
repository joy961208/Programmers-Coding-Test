def solution(d, budget):
    answer = 0
    a = sorted(d)
    for i in a:
        budget -= i
        if budget <0:
            break
        answer += 1
    return answer