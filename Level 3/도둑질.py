def solution(money):
    dp1 = money.copy()
    dp2 = money.copy()
    dp1[0] = money[0]
    dp1[1] = max(money[0:2])
    dp2[0] = 0

    for i in range(2, len(money)):
        if i != len(money) - 1:
            dp1[i] = max(dp1[i - 1], dp1[i] + dp1[i - 2])
        dp2[i] = max(dp2[i - 1], dp2[i] + dp2[i - 2])

    return max(max(dp1), max(dp2))
