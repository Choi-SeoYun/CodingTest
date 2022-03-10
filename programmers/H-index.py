def solution(citations):
    answer = 0
    n = len(citations)
    
    for i in range(n, 0, -1):
        citations.append(i)
        citations = sorted(citations)
        idx = citations.index(i)
        
        if n-idx >= i and idx <= i:
            return i
        
    return answer