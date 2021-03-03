def change2(a, n):  # 2진수로 바꿔주는 함수
    b = []
    for i in range(n):
        b.append(a % 2)
        a = a // 2
    b.reverse()
    return b


def solution(n, arr1, arr2):
    answer = []
    a = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(arr1)):
        li1 = change2(arr1[i], n)
        li2 = change2(arr2[i], n)
        answer.append([li1[j] | li2[j] for j in range(len(li1))])
    ans = []

    for i in answer:
        an = ""

        for j in i:
            if j == 1:
                an += "#"
            else:
                an += " "

        ans.append(an)

    return ans