import math
def solution(brown, yellow):
    answer = []
    a = brown - 4
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow%i == 0:
            if (i+int(yellow//i)) * 2 == a:
                answer.append(i+2)
                answer.append(yellow//i + 2)
    answer.sort(reverse=True)
    return answer