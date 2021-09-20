
def solution(stones, k):
    m = max(stones)
    n = 1
    
    while m-n > 1:
        c = 0
        a = 0
        r = (m+n)//2

        for i in stones:
            if i-r <= 0 :
                c+=1
            else:
                c = 0
            if c >= k:
                a = 1
                break
        if a == 0:
            n = (m+n)//2
        else:
            m = (m+n)//2
    return m
