# (주의) 정답 아님
def solution(name):
    answer = 0
    
    # 상하
    for i in name:
        answer += min(ord(i)-ord('A'), 26-(ord(i)-ord('A')))
    
    # 좌우
    if len(name)>=2:
        if name[-1] == 'A':
            name_2 = name.rstrip('A')
            answer += len(name_2) - 1
        elif name[1] == 'A':
            name_2 = name[1:].lstrip('A')
            answer += len(name_2)
        else:
            answer += len(name) - 1
    else:
        answer+=0

    return answer

print(solution("BABBBB"))