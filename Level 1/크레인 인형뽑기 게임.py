def solution(board, moves):
    answer = 0
    a = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else :
                if len(a) > 0:
                    if board[j][i-1] == a[-1]:
                        del a[-1]
                        answer += 2
                    else:
                        a.append(board[j][i-1])
                else :
                    a.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer