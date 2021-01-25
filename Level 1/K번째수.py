def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        li = commands[i]
        a = sorted(array[li[0]-1:li[1]])
        answer.append(a[li[2]-1])
    return answer