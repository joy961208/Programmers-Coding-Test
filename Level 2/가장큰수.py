def solution(numbers):
    numbers = list(map(str,numbers))
    # 1000이하의 숫자이므로 3번 문자열을 반복해줌으로써 우선순위를 정해준다.
    # ex) 9와 90 이있을때 9가 앞에있어야 더 큰수가 되지만 '90'>'9'이다. 이때 문자열을 반복해줘서 '999' > '909090'이 된다.
    numbers = sorted(numbers,key = lambda x : x*3)
    numbers.reverse()
    return str(int(''.join(numbers)))
