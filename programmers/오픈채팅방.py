def solution(record):
    answer = []
    table = {}
    
    for i in record:
        content = i.split()
        if content[0]=='Change' or content[0]=='Enter':
            table[content[1]] = content[2]
    
    for i in record:
        content = i.split()
        if content[0]=='Enter':
            answer.append(f"{table[content[1]]}님이 들어왔습니다.")
        if content[0]=='Leave':
            answer.append(f"{table[content[1]]}님이 나갔습니다.")      
    
    return answer