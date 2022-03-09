from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque((n, i) for i,n in enumerate(priorities))
    
    while queue:
        j = queue.popleft()
        
        if queue and max(queue)[0] > j[0]:
            queue.append(j)
        else:
            answer += 1
            if j[1] == location:
                break
            
    return answer