def solution(citations):
    answer = 0
    for i in range(0,len(citations)+1):
        a = 0
        for j in citations:
            if j >= i:
                a += 1
        if a >= i:
            answer = i

    return answer