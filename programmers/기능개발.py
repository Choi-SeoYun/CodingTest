import numpy as np

def solution(progresses, speeds):
    answer = []
    
    hundred = np.full(len(progresses), 100)
    np_progresses = np.array(progresses)
    np_speeds = np.array(speeds)
    
    left_days = np.ceil((hundred - np_progresses) / np_speeds)
    print(left_days)
    
    num=1
    last_day = left_days[0]
    for i in range(1, len(left_days)):
        if last_day >= left_days[i]:
            num+=1
            if i == len(left_days)-1:
                answer.append(num)
        else:
            answer.append(num)
            num=1
            last_day = left_days[i]
            if i == len(left_days)-1:
                answer.append(1)
    
    return answer