def solution(s):
    answer = []
    
    for i in range(len(s)):
        if len(answer)==0 or (answer[-1] != s[i]):
            answer.append(s[i])
        else:
            answer.pop()
            
    if len(answer) > 0:
        return 0
    else:
        return 1