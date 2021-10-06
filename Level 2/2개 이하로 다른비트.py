def binary(number):
    a = "" 
    while number != 0:
        a = str(number % 2) + a
        number = number//2
    return a

def decimal(number):
    a = 0
    for i, v in enumerate(number):
        a += 2 ** (len(number)-1 - i)  * int(v)
    return a


def solution(numbers):
    answer = []
    for i in numbers:
        if i %2 ==0:
            answer.append(i+1)
        else:
            num = binary(i)
            num = list(num)
            if "0" not in num:
                num.insert(0, "1")
                num[1] = "0"
            else:
                num = list(reversed(num))
                ind = num.index("0")
                num[ind] = "1"
                num[ind-1] = "0"
                num = list(reversed(num))
            answer.append(decimal(num))
            
    return answer

