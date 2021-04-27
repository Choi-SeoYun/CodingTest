from collections import Counter
def solution(participant, completion):
    answer = ''
    
    answer = list(Counter(participant) - Counter(completion))[0]
    
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))