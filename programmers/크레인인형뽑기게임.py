def solution(board, moves):
    answer = 0
    sol = []

    for i in moves:     #차례대로 가니까 moves를 지울 필요는 없음
        for j in range(len(board)):
            if board[j][i-1] > 0:
                p = board[j][i-1]
                board[j][i-1] = 0
                if len(sol) == 0:
                    sol.append(p)
                    break
                elif sol[len(sol)-1] == p:
                    del sol[len(sol)-1]
                    answer += 2
                    break
                else:
                    sol.append(p)
                    break
            else:
                continue
            
    return answer