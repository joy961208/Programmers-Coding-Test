def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers = sorted(numbers,key = lambda x : x*3)
    numbers.reverse()
    answer = str(int(''.join(numbers)))
    return answer
