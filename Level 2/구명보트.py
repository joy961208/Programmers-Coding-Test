def solution(people, limit):
    answer = 0
    people.sort(reverse = 1)
    a = 0
    b = len(people) -1

    while True:
        if people[a] + people[b] <= limit:
            a += 1
            b -= 1
        else:
            a+=1
        answer += 1
        if a == b:
            answer += 1
            break
        elif a>b:
            break

    return answer
