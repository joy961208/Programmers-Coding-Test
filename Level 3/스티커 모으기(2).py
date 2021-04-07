def solution(sticker):
    
    if len(sticker) <=3:
        return max(sticker)
    
    dp1 = sticker.copy()
    dp2 = sticker.copy()
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0:2])
    dp2[0] = 0

    for i in range(2, len(sticker)):

        if i != len(sticker) - 1:
            dp1[i] = max(dp1[i - 1], dp1[i] + dp1[i - 2])
        dp2[i] = max(dp2[i - 1], dp2[i] + dp2[i - 2])


    return max(max(dp1),max(dp2))
