from itertools import combinations

def solution(orders, course):
    answer = []

    for j,i in enumerate(orders):
        orders[j] = sorted(list(i))

    for i in course:
        a = []

        for j in orders:
            if len(j) >= i:
                a.extend(list(combinations(list(j),i)))

        b = sorted(a,key = lambda x : a.count(x),reverse= 1)

        if len(b) != 0 and b.count(b[0]) >= 2:
            answer.append("".join(b[0]))
            c=0
            while True:
                if c != len(b) - 1 and a.count(b[c]) == a.count(b[c+1]):
                    answer.append("".join(b[c+1]))
                    c += 1
                else:
                    break
    answer = list(set(answer))
    answer.sort()
    return answer