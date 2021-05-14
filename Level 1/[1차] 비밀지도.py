
def solution(n, arr1, arr2):
    ans = []

    for i in range(n):
        bb = ""
        a1 = arr1[i]
        a2 = arr2[i]
        for j in range(n):
            if a1%2 == 1 or a2%2 == 1:
                bb = "#" + bb
            else:
                bb = " " + bb
            a1 //= 2
            a2 //= 2

        ans.append(bb)
    return ans
