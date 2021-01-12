def change3(n):  # 3진법 변환
    li = []
    a = ''
    while n != 0:
        li.append(str(n % 3))
        n = n // 3
    for i in li:
        a += i
    return int(a)  # a는 앞뒤를 반전시킨 3진법수


def change10(n):  # 10진법변환
    li = list(str(n))
    li.reverse()
    c = 0
    a = 0
    for i in li:
        a += int(i) * (3 ** c)
        c += 1
    return a


def solution(n):
    answer = change3(n)
    answer = change10(answer)

    return answer
