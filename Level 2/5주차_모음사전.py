def solution(word):
    answer = 0
    num_list = [781,156,31,6,1]
    
    for j,i in enumerate(word):
        if i == "A":
            answer += num_list[j] * 0 + 1
        elif i == "E":
            answer += num_list[j] * 1 + 1
        elif i == "I":
            answer += num_list[j] * 2 + 1
        elif i == "O":
            answer += num_list[j] * 3 + 1
        elif i == "U":
            answer += num_list[j] * 4 + 1

    return answer
