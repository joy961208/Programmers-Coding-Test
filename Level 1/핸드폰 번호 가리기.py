def solution(phone_number):
    a = list(phone_number)
    answer = ""
    for i in range(len(a)-4):
        answer += "*"
    for i in a[-4:]:
        answer+=i
    return answer