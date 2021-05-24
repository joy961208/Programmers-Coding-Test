def solution(words):
    answer = 0
    words.sort()

    for i,j in enumerate(words[0]):
        if i == len(words[1]):
            answer += 1
            break
        if j == words[1][i] :
            answer += 1
        else:
            answer += 1
            break
    a = 1
    while True:
        c1 = 0
        c2 = 0

        for i,j in enumerate(words[a]):
            if i == len(words[a+1]):
                c1 +=1
                break
            if j == words[a+1][i]:
                c1 += 1
            else:
                c1 += 1
                break

        for i,j in enumerate(words[a]):
            if i == len(words[a-1]):
                c2 +=1
                break
            if j == words[a-1][i]:
                c2 += 1
            else:
                c2 += 1
                break
        answer += max(c1,c2)
        a += 1
        
        if a == len(words) -1:
            for i, j in enumerate(words[a]):
                if i == len(words[a - 1]):
                    answer += 1
                    break
                if j == words[a - 1][i]:
                    answer += 1
                else:
                    answer += 1
                    break
            return answer
    return answer
