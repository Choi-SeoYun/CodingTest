def solution(array, commands):
    answer = []
    for i in commands:
        cut_array = sorted(array[i[0]-1:i[1]])
        
        answer.append(cut_array[i[-1]-1])
    return answer