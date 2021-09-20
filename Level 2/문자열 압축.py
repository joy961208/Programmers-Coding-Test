def solution(s):
    answer = len(s)
    
    for i in range(1,(len(s)//2)+1):
        a = [s[j:j+i] for j in range(0,len(s),i)]
        c = 1
        st = ""
        
        for j,v in enumerate(a[:-1]):
            if v == a[j+1]:
                c += 1
            else:
                if c != 1:
                    st += str(c) + v
                    c = 1
                else:
                    st += v
        if c != 1:
            st += str(c) + a[-1]
        else:
            st += a[-1]

        if len(st) < answer:
            answer = len(st)
    return answer
