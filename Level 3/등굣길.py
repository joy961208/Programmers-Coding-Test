def solution(m, n, puddles):
    answer = 0
    dic = {}
    a = 1
    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] not in puddles:
                dic[a] = 0
            a+=1

    for i in range(1,m*n + 1):
        if i in dic :
            if i <= m :
                if i == 1:
                    dic[i] = 1
                elif i-1 in dic:
                    dic[i] = dic[i-1]
            elif i%m == 1:
                if i == m+1:
                    dic[i] = 1
                elif i-m in dic:
                    dic[i] = dic[i-m]

            else:
                if i-1 in dic and i - m in dic:
                    dic[i] = dic[i - 1] + dic[i - m]
                elif i-1 in dic:
                    dic[i] = dic[i - 1]
                elif i-m in dic:
                    dic[i] = dic[i-m]
                else:
                    dic[i] = 0


    return dic[m*n] % 1000000007