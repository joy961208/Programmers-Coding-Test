def sol(a, b):
    k = abs(b - a)
    c = 0
    while k != 0:
        if k % 3 == 0:
            k -= 3
            c += 1
        else:
            k -= 1
            c += 1
    return c


def solution(numbers, hand):
    answer = ''
    L = 10
    R = 12
    for j in numbers:
        if j == 0:
            i = 11
        else:
            i = j
        if i in [1, 4, 7]:
            answer += 'L'
            L = i
        elif i in [3, 6, 9]:
            answer += 'R'
            R = i
        else:
            if sol(i, R) > sol(i, L):
                L = i
                answer += 'L'
            elif sol(i, R) < sol(i, L):
                R = i
                answer += 'R'
            else:
                if hand == "right":
                    R = i
                    answer += 'R'
                else:
                    L = i
                    answer += 'L'

    return answer