def solution(A, B):
    A.sort()
    B.sort(reverse = True)
    answer = []
    i = 0
    
    while True:
        if A[i] < B[-1]:
            answer.append(B[-1])
            B.pop()
            i += 1
            
        else:
            B.pop()
        if i == len(A) or B == []:
            break
            
    return len(answer)
