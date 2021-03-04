def mm(a):
    i = max(a)
    for j in a:
        if j != 0 and j<i:
            i = j
    return i

def solution(stones, k):
    answer = 0
    b = 0
    while True:
        a = mm(stones)
        answer += a
        st = stones.copy()
        stones = []
        for i in st:
            if i != 0 :
                stones.append(i-a)
            else:
                stones.append(0)
        for i in range(len(stones)-k):
            if sum(stones[i:i+k]) == 0:
                b = 1
                break
        if b == 1:
            break
    return answer