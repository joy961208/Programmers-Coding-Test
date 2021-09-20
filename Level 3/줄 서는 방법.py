import math
def solution(n, k):
    answer = []
    f = math.factorial(n)
    numlist = [i for i in range(1,n+1)]
    c = n
    
    while True:
        z = f/n
        for i in range(1,n+1):
            if k < z*i:
                k -= z*(i-1)
                f = f/n
                answer.append(numlist[i-1])
                numlist.pop(i-1)
                break
                
            elif k == z*i:
                answer.append(numlist[i - 1])
                numlist.pop(i - 1)
                numlist.reverse()
                for j in numlist:
                    if j not in answer:
                        answer.append(j)
                return answer
        n -= 1
        if len(answer) == c:
            break
    return answer
