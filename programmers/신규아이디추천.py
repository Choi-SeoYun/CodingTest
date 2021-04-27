def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    str_list = ['-', '_', '.']
    for i in new_id:
        if i.isalpha() or i in str_list or i.isdigit():
            answer += i
    print(answer)
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if len(answer) == 0:
        answer += 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7단계
    if len(answer) <= 2:
        last_c = answer[-1]
        while len(answer) < 3:
            answer += last_c
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
# "bat.y.abcdefghi"