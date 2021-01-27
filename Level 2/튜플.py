from collections import Counter
def solution(s):
    answer = []
    ans = list(map(int,s.replace("{","").replace("}","").split(",")))
    coun = Counter(ans)
    ans.sort(key = lambda x : coun[x],reverse=True)

    for i in ans:

        if i  not in answer:
            answer.append(i)

    return answer