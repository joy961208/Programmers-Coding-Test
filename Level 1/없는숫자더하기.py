def solution(numbers):
    number_li = [i for i in range(0,10)]
    for i in numbers:
        number_li.remove(i)
        
    return sum(number_li)
