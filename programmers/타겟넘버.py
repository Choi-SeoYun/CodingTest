from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])
    
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

"""
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
"""
from itertools import product

_list = ["012", "abc", "!@#"]
pd_1 = list(product(*_list))
pd_2 = list(product(_list))

print(pd_1)    # [('0', 'a', '!'), ('0', 'a', '@'), ('0', 'a', '#'), ('0', 'b', '!'), ('0', 'b', '@'), ('0', 'b', '#'), ('0', 'c', '!'), ('0', 'c', '@'), ('0', 'c', '#'), ('1', 'a', '!'), ('1', 'a', '@'), ('1', 'a', '#'), ('1', 'b', '!'), ('1', 'b', '@'), ('1', 'b', '#'), ('1', 'c', '!'), ('1', 'c', '@'), ('1', 'c', '#'), ('2', 'a', '!'), ('2', 'a', '@'), ('2', 'a', '#'), 
#('2', 'b', '!'), ('2', 'b', '@'), ('2', 'b', '#'), ('2', 'c', '!'), ('2', 'c', '@'), ('2', 'c', '#')]
print("-"*50)
print(pd_2)    # [('012',), ('abc',), ('!@#',)]